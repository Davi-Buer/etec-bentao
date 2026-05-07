# 👨‍🏫 Setup do Instrutor - Preparação do Ambiente

Guia passo a passo para preparar o ambiente Azure antes da aula.

## 📋 Pré-requisitos

- ✅ Resource Group criado: `etec-bentao`
- ✅ Azure CLI instalado
- ✅ Permissões de Owner ou Contributor na subscription

---

## 🚀 Parte 1: Aplicar Azure Policy

### Passo 1: Fazer Login no Azure

```bash
# Login no Azure
az login

# Listar subscriptions disponíveis
az account list --output table

# Selecionar a subscription correta (se tiver múltiplas)
az account set --subscription "NOME-OU-ID-DA-SUBSCRIPTION"

# Verificar qual subscription está ativa
az account show --output table
```

---

### Passo 2: Verificar o Resource Group

```bash
# Ver detalhes do RG
az group show --name etec-bentao --output table

# Listar recursos existentes no RG (deve estar vazio ou quase)
az resource list --resource-group etec-bentao --output table
```

**Saída esperada:**
```
Name         Location     Status
-----------  -----------  --------
etec-bentao  brazilsouth  Succeeded
```

---

### Passo 3: Criar a Policy Definition

```bash
# Entrar na pasta do repositório
cd etec-bentao

# Criar a policy definition
az policy definition create \
  --name 'Policy-Controle-Custos-ETEC' \
  --display-name 'Controle de Custos - ETEC Bentão' \
  --description 'Bloqueia recursos caros e garante conformidade para alunos' \
  --rules @azure/policy/policy.json \
  --mode All

# Verificar se foi criada
az policy definition list \
  --query "[?displayName=='Controle de Custos - ETEC Bentão']" \
  --output table
```

**Saída esperada:**
```
Name                         Type            DisplayName
---------------------------  --------------  ---------------------
Policy-Controle-Custos-ETEC  Custom          Controle de Custos...
```

---

### Passo 4: Atribuir Policy ao Resource Group

```bash
# Pegar o ID do Resource Group
RG_ID=$(az group show --name etec-bentao --query id --output tsv)

echo "RG ID: $RG_ID"

# Atribuir a policy ao RG etec-bentao
az policy assignment create \
  --name 'aplicar-controle-custos-etec' \
  --display-name 'Aplicar Controle de Custos - ETEC Bentão' \
  --policy 'Policy-Controle-Custos-ETEC' \
  --scope "$RG_ID"

# Verificar se foi atribuída
az policy assignment list \
  --resource-group etec-bentao \
  --output table
```

**Saída esperada:**
```
Name                          ResourceGroup  DisplayName
----------------------------  -------------  ----------------------
aplicar-controle-custos-etec  etec-bentao    Aplicar Controle de...
```

---

### Passo 5: Testar a Policy

**Teste 1: Tentar criar VM grande (deve bloquear) ❌**

```bash
# Tentar criar VM D2s_v3 (cara!)
az vm create \
  --resource-group etec-bentao \
  --name vm-teste-grande \
  --image Ubuntu2204 \
  --size Standard_D2s_v3 \
  --admin-username azureuser \
  --generate-ssh-keys
```

**Resultado esperado:**
```
❌ ERROR: Resource creation was disallowed by policy.
Policy: Policy-Controle-Custos-ETEC
Reason: VM size 'Standard_D2s_v3' is not allowed.
```

✅ **Funcionou! Policy está bloqueando VMs caras!**

---

**Teste 2: Criar VM pequena (deve permitir) ✅**

```bash
# Criar VM B1s (permitida)
az vm create \
  --resource-group etec-bentao \
  --name vm-teste-ok \
  --image Ubuntu2204 \
  --size Standard_B1s \
  --admin-username azureuser \
  --generate-ssh-keys

# Depois de testar, delete a VM
az vm delete \
  --resource-group etec-bentao \
  --name vm-teste-ok \
  --yes
```

**Resultado esperado:**
```
✅ Deployment succeeded
```

✅ **Perfeito! Policy permite VMs pequenas!**

---

### Passo 6: Testar Bloqueio de Região

```bash
# Tentar criar Storage Account em East US (deve bloquear)
az storage account create \
  --name sttesteetec \
  --resource-group etec-bentao \
  --location eastus \
  --sku Standard_LRS
```

**Resultado esperado:**
```
❌ ERROR: Resource creation was disallowed by policy.
Reason: Location 'eastus' is not allowed.
Allowed locations: brazilsouth, brazilsoutheast, global
```

✅ **Policy bloqueando regiões não-brasileiras!**

---

## 🎯 Parte 2: Configurar Budget Alerts

### Criar Alerta de Custo

```bash
# Pegar o ID da subscription
SUBSCRIPTION_ID=$(az account show --query id --output tsv)

# Criar budget de R$ 500/mês para o RG
az consumption budget create \
  --budget-name budget-etec-bentao \
  --category cost \
  --amount 500 \
  --time-grain monthly \
  --start-date $(date +%Y-%m-01) \
  --resource-group etec-bentao

# Criar alerta quando atingir 80% (R$ 400)
az consumption budget create \
  --budget-name budget-etec-bentao \
  --category cost \
  --amount 500 \
  --time-grain monthly \
  --start-date $(date +%Y-%m-01) \
  --resource-group etec-bentao \
  --notifications \
    "Actual_GreaterThan_80_Percent={enabled:true,operator:GreaterThan,threshold:80,contactEmails:[SEU-EMAIL@dominio.com]}"
```

💡 **Substitua `SEU-EMAIL@dominio.com` pelo seu email!**

---

## 👥 Parte 3: Preparar Acesso para Alunos

### Opção A: Cada Aluno com Usuário Próprio

**1. Convidar alunos para a organização Azure:**

Via Portal:
1. Azure Active Directory → Users
2. New user → Invite external user
3. Email do aluno
4. Role: Contributor (apenas no RG etec-bentao)

Via CLI:
```bash
# Convidar aluno
az ad user create \
  --display-name "João Silva" \
  --user-principal-name joao.silva@SEU-DOMINIO.onmicrosoft.com \
  --password "SenhaTemporaria123!" \
  --force-change-password-next-login true

# Dar permissão de Contributor no RG
az role assignment create \
  --assignee joao.silva@SEU-DOMINIO.onmicrosoft.com \
  --role Contributor \
  --resource-group etec-bentao
```

---

### Opção B: Conta Compartilhada (Mais Simples)

**1. Criar uma conta `aluno@etec` para todos compartilharem:**

1. No Portal Azure → Azure AD → Users → New user
2. User name: `aluno@SEU-DOMINIO.onmicrosoft.com`
3. Password: `EtecBentao2024!` (ou outro seguro)
4. Role: Contributor no RG `etec-bentao`

**2. Compartilhar credenciais com os alunos:**

```
Portal: https://portal.azure.com
Usuário: aluno@SEU-DOMINIO.onmicrosoft.com
Senha: EtecBentao2024!
Resource Group: etec-bentao
```

⚠️ **IMPORTANTE:** Com conta compartilhada, use convenção de nomes:
- VM: `vm-aluno-SEUNOME` (ex: `vm-aluno-joao`)
- Storage: `stalgSEUNOME` (ex: `stalgjoao`)
- App Service: `app-aluno-SEUNOME` (ex: `app-aluno-joao`)

Isso evita conflitos entre alunos!

---

## 📊 Parte 4: Monitorar Durante a Aula

### Ver Recursos Criados

```bash
# Listar todos os recursos no RG
az resource list \
  --resource-group etec-bentao \
  --output table

# Ver apenas VMs
az vm list \
  --resource-group etec-bentao \
  --output table \
  --query "[].{Name:name, Size:hardwareProfile.vmSize, Status:powerState}"

# Ver Storage Accounts
az storage account list \
  --resource-group etec-bentao \
  --output table

# Ver App Services
az webapp list \
  --resource-group etec-bentao \
  --output table
```

---

### Ver Custos em Tempo Real

```bash
# Ver custo acumulado do RG até agora
az consumption usage list \
  --resource-group etec-bentao \
  --start-date $(date -d "1 month ago" +%Y-%m-%d) \
  --end-date $(date +%Y-%m-%d) \
  --query "[].{Date:usageStart, Cost:pretaxCost}" \
  --output table
```

**Via Portal (mais fácil):**
1. Vá em "Cost Management + Billing"
2. "Cost analysis"
3. Filtro: Resource group = `etec-bentao`
4. Veja os gastos em tempo real!

---

### Ver Compliance da Policy

```bash
# Ver recursos em conformidade
az policy state list \
  --resource-group etec-bentao \
  --query "[?complianceState=='NonCompliant']" \
  --output table
```

**Via Portal:**
1. Azure Policy
2. Compliance
3. Filtro: `etec-bentao`
4. Veja quais recursos violam a policy

---

## 🧹 Parte 5: Limpeza Pós-Aula

### Deletar Todos os Recursos (Manter RG)

```bash
# Listar tudo que será deletado
az resource list \
  --resource-group etec-bentao \
  --query "[].{Name:name, Type:type}" \
  --output table

# ATENÇÃO: Isso deleta TUDO no RG!
# Pare VMs primeiro para economizar imediatamente
az vm deallocate --ids $(az vm list -g etec-bentao --query "[].id" -o tsv)

# Depois delete todos os recursos
az resource list \
  --resource-group etec-bentao \
  --query "[].id" \
  --output tsv | xargs -I {} az resource delete --ids {} --verbose
```

⚠️ **Cuidado:** Isso deleta TODOS os recursos dos alunos!

---

### Deletar RG Completamente (Fim do Curso)

```bash
# ATENÇÃO: Deleta RG + Policy + Tudo!
az group delete \
  --name etec-bentao \
  --yes \
  --no-wait

# Deletar a policy definition também
az policy assignment delete \
  --name aplicar-controle-custos-etec \
  --resource-group etec-bentao

az policy definition delete \
  --name Policy-Controle-Custos-ETEC
```

---

## 📋 Checklist Final

**Antes da aula:**
- [ ] Resource Group `etec-bentao` criado
- [ ] Policy aplicada e testada
- [ ] Budget alert configurado
- [ ] Contas de alunos criadas (ou conta compartilhada)
- [ ] Testar: criar VM B1s (deve funcionar)
- [ ] Testar: criar VM grande (deve bloquear)
- [ ] Credenciais compartilhadas com alunos

**Durante a aula:**
- [ ] Monitorar custos em tempo real
- [ ] Ajudar alunos com problemas
- [ ] Ver compliance da policy

**Depois da aula:**
- [ ] Parar (deallocate) todas as VMs
- [ ] Avaliar se deleta recursos ou mantém para próxima aula
- [ ] Revisar custos finais

---

## 💰 Estimativa de Custos

**Por aluno (worst case - tudo ligado 24/7 por 30 dias):**
- VM B1s: R$ 30/mês
- Storage LRS: R$ 5/mês
- App Service F1: Grátis
- Key Vault: < R$ 5/mês
- **Total: ~R$ 40/aluno/mês**

**30 alunos × R$ 40 = R$ 1.200/mês (máximo)**

**Com boas práticas (VMs desligadas à noite):**
- VM ligada 8h/dia útil: R$ 8/mês
- **Total: ~R$ 15/aluno/mês**
- **30 alunos = R$ 450/mês** ✅

**Com a policy:**
- ✅ Impossível gastar mais que o limite!
- ✅ Sem surpresas

---

## 🆘 Troubleshooting

### Policy não está bloqueando
```bash
# Verificar se está ativa
az policy assignment show \
  --name aplicar-controle-custos-etec \
  --resource-group etec-bentao

# Ver logs de deny
az policy state list \
  --resource-group etec-bentao \
  --filter "complianceState eq 'NonCompliant'"
```

### Aluno não consegue criar recurso permitido
1. Verificar se tem permissão de Contributor no RG
2. Aguardar 5-10 min (policy demora a propagar)
3. Verificar se o nome do recurso é único

### Custos muito altos
1. Ver "Cost Management" no portal
2. Identificar recursos caros
3. Parar VMs: `az vm deallocate`
4. Deletar recursos desnecessários

---

## 📞 Suporte

**Durante a aula:**
- Grupo WhatsApp: https://chat.whatsapp.com/JLKp1OqAOa03Nc1iN8F1kb
- Discord ToolBox: https://discord.gg/vGfZj7QBwC

**Documentação:**
- Este repositório: README.md
- Azure Docs: https://docs.microsoft.com/azure

---

**Feito com 💙 pela equipe [ToolBox Technology](https://tbxtech.com.br/)**

**Boa aula! 🚀**
