#!/bin/bash
#
# Script para aplicar a Azure Policy no Resource Group etec-bentao
# Uso: bash apply-policy.sh
#

set -e

echo "🔐 Aplicando Azure Policy de Controle de Custos"
echo "================================================"
echo ""

# Verificar se Azure CLI está instalado
if ! command -v az &> /dev/null; then
    echo "❌ Azure CLI não encontrado!"
    echo "   Instale: https://docs.microsoft.com/cli/azure/install-azure-cli"
    exit 1
fi

# Verificar se está logado
echo "🔍 Verificando login no Azure..."
if ! az account show &> /dev/null; then
    echo "⚠️  Você não está logado no Azure!"
    echo "   Executando: az login"
    az login
fi

# Mostrar account atual
echo ""
echo "✅ Logado no Azure:"
az account show --query '{Nome:name, ID:id, Usuario:user.name}' --output table
echo ""

# Confirmar se é a subscription correta
read -p "Esta é a subscription correta? (s/n): " confirm
if [[ $confirm != "s" ]]; then
    echo "❌ Operação cancelada."
    echo "   Use: az account set --subscription 'NOME-OU-ID'"
    exit 1
fi

# Verificar se o RG existe
RG_NAME="etec-bentao"
echo ""
echo "🔍 Verificando Resource Group '$RG_NAME'..."

if ! az group show --name $RG_NAME &> /dev/null; then
    echo "❌ Resource Group '$RG_NAME' não encontrado!"
    echo ""
    read -p "Deseja criar o Resource Group agora? (s/n): " create_rg
    if [[ $create_rg == "s" ]]; then
        echo "📦 Criando Resource Group '$RG_NAME' em Brazil South..."
        az group create --name $RG_NAME --location brazilsouth
        echo "✅ Resource Group criado!"
    else
        echo "❌ Operação cancelada."
        exit 1
    fi
else
    echo "✅ Resource Group '$RG_NAME' encontrado!"
fi

# Listar recursos existentes
echo ""
echo "📊 Recursos existentes no RG:"
RESOURCE_COUNT=$(az resource list --resource-group $RG_NAME --query "length([])" --output tsv)
if [ "$RESOURCE_COUNT" -eq 0 ]; then
    echo "   (nenhum recurso ainda)"
else
    az resource list --resource-group $RG_NAME --query "[].{Nome:name, Tipo:type}" --output table
fi

# Confirmar aplicação da policy
echo ""
echo "⚠️  ATENÇÃO: A policy vai bloquear:"
echo "   - VMs maiores que B1s, B1ms, B2s"
echo "   - App Services maiores que F1, B1"
echo "   - Storage Premium"
echo "   - Recursos fora de Brazil South/Southeast"
echo ""
read -p "Continuar com a aplicação da policy? (s/n): " confirm_policy
if [[ $confirm_policy != "s" ]]; then
    echo "❌ Operação cancelada."
    exit 1
fi

# Verificar se arquivos existem
POLICY_RULE_FILE="$(dirname "$0")/policy-rule.json"
POLICY_METADATA_FILE="$(dirname "$0")/policy-metadata.json"

if [ ! -f "$POLICY_RULE_FILE" ]; then
    echo "❌ Arquivo policy-rule.json não encontrado!"
    echo "   Procurado em: $POLICY_RULE_FILE"
    exit 1
fi

if [ ! -f "$POLICY_METADATA_FILE" ]; then
    echo "❌ Arquivo policy-metadata.json não encontrado!"
    echo "   Procurado em: $POLICY_METADATA_FILE"
    exit 1
fi

echo ""
echo "📋 Criando Policy Definition..."

# Deletar policy antiga se existir (para atualizar)
if az policy definition show --name 'Policy-Controle-Custos-ETEC' &> /dev/null; then
    echo "⚠️  Policy definition já existe. Deletando versão antiga..."

    # Deletar assignments primeiro
    ASSIGNMENTS=$(az policy assignment list --query "[?policyDefinitionId contains(@, 'Policy-Controle-Custos-ETEC')].name" --output tsv)
    if [ ! -z "$ASSIGNMENTS" ]; then
        echo "   Deletando assignments existentes..."
        for assignment in $ASSIGNMENTS; do
            az policy assignment delete --name "$assignment" &> /dev/null || true
        done
    fi

    # Deletar definition
    az policy definition delete --name 'Policy-Controle-Custos-ETEC' &> /dev/null || true
fi

# Criar nova policy definition
az policy definition create \
  --name 'Policy-Controle-Custos-ETEC' \
  --display-name 'Controle de Custos - ETEC Bentão' \
  --description 'Bloqueia recursos caros e garante conformidade para alunos' \
  --rules @"$POLICY_RULE_FILE" \
  --metadata @"$POLICY_METADATA_FILE" \
  --mode All

echo "✅ Policy definition criada!"

# Pegar ID do Resource Group
RG_ID=$(az group show --name $RG_NAME --query id --output tsv)

echo ""
echo "🔗 Atribuindo Policy ao Resource Group..."

# Criar assignment
az policy assignment create \
  --name 'aplicar-controle-custos-etec' \
  --display-name 'Aplicar Controle de Custos - ETEC Bentão' \
  --policy 'Policy-Controle-Custos-ETEC' \
  --scope "$RG_ID"

echo "✅ Policy atribuída ao RG '$RG_NAME'!"

# Aguardar propagação
echo ""
echo "⏳ Aguardando propagação da policy (10 segundos)..."
sleep 10

# Verificar assignment
echo ""
echo "📊 Verificando policy aplicada:"
az policy assignment list --resource-group $RG_NAME --output table

echo ""
echo "================================================"
echo "✅ Policy aplicada com sucesso!"
echo "================================================"
echo ""
echo "🧪 PRÓXIMOS PASSOS:"
echo ""
echo "1️⃣  Testar bloqueio de VM grande:"
echo "   az vm create \\"
echo "     --resource-group $RG_NAME \\"
echo "     --name vm-teste-grande \\"
echo "     --image Ubuntu2204 \\"
echo "     --size Standard_D2s_v3 \\"
echo "     --admin-username azureuser \\"
echo "     --generate-ssh-keys"
echo ""
echo "   Resultado esperado: ❌ BLOQUEADO pela policy"
echo ""
echo "2️⃣  Testar criação de VM permitida:"
echo "   az vm create \\"
echo "     --resource-group $RG_NAME \\"
echo "     --name vm-teste-ok \\"
echo "     --image Ubuntu2204 \\"
echo "     --size Standard_B1s \\"
echo "     --admin-username azureuser \\"
echo "     --generate-ssh-keys"
echo ""
echo "   Resultado esperado: ✅ PERMITIDO pela policy"
echo ""
echo "3️⃣  Ver compliance:"
echo "   Portal Azure → Policy → Compliance → Filtro: $RG_NAME"
echo ""
echo "📖 Documentação completa: docs/setup-instrutor.md"
echo ""
