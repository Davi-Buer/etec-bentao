#!/bin/bash
#
# Script para fazer deploy da aplicação Docker Compose na VM Azure
# Este script clona o repositório e configura o app Node.js + Redis
#
# Uso:
#   bash deploy-docker-app.sh

set -e

echo "🚀 Deploy da aplicação Docker Compose na VM Azure"
echo ""

# Verificar se Docker está instalado
if ! command -v docker &> /dev/null; then
    echo "❌ Docker não encontrado!"
    echo "Execute primeiro: bash setup-vm.sh"
    exit 1
fi

# Verificar se está no grupo docker
if ! groups | grep -q docker; then
    echo "❌ Você não está no grupo docker!"
    echo "Faça logout e login novamente, depois execute este script."
    exit 1
fi

# Criar pasta de projetos se não existir
mkdir -p ~/projects
cd ~/projects

# Clonar repositório (ajuste a URL conforme necessário)
echo "📥 Clonando repositório..."
REPO_URL="https://github.com/toolbox-playground/etec-bentao.git"
REPO_DIR="etec-bentao"

if [ -d "$REPO_DIR" ]; then
    echo "⚠️  Repositório já existe. Atualizando..."
    cd $REPO_DIR
    git pull
else
    git clone $REPO_URL
    cd $REPO_DIR
fi

# Configurar porta (cada aluno deve usar uma porta diferente)
echo ""
echo "🔧 Configurando porta da aplicação..."
read -p "Digite a porta para sua aplicação (ex: 8001, 8002, 8003): " APP_PORT

# Criar arquivo .env
cat > .env << EOF
APP_PORT=${APP_PORT}
EOF

echo "✅ Porta configurada: $APP_PORT"

# Construir e iniciar containers
echo ""
echo "🐳 Construindo e iniciando containers..."
docker compose up -d --build

# Aguardar containers iniciarem
echo "⏳ Aguardando containers iniciarem..."
sleep 5

# Verificar status
echo ""
echo "📊 Status dos containers:"
docker compose ps

# Pegar IP público da VM
PUBLIC_IP=$(curl -s ifconfig.me)

echo ""
echo "=============================================="
echo "✅ Deploy concluído com sucesso!"
echo "=============================================="
echo ""
echo "🌐 Acesse sua aplicação em:"
echo "   http://$PUBLIC_IP:$APP_PORT"
echo ""
echo "⚠️  IMPORTANTE: Certifique-se de que a porta $APP_PORT"
echo "   está aberta no Network Security Group (NSG) do Azure!"
echo ""
echo "📋 Para abrir a porta no Azure:"
echo "   1. Vá no Portal Azure"
echo "   2. Vá em Virtual Machines > sua-vm"
echo "   3. Vá em Networking > Add inbound port rule"
echo "   4. Adicione a porta $APP_PORT"
echo ""
echo "🛠️  Comandos úteis:"
echo "   Ver logs:          docker compose logs -f"
echo "   Parar containers:  docker compose down"
echo "   Reiniciar:         docker compose restart"
echo "   Ver status:        docker compose ps"
echo ""
