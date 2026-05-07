#!/bin/bash
#
# Script de setup inicial para VM Ubuntu no Azure
# Execute este script após criar a VM para configurar o ambiente básico
#
# Uso:
#   curl -fsSL https://raw.githubusercontent.com/SEU-REPO/etec-bentao/main/azure/vm/setup-vm.sh | bash
#   ou
#   bash setup-vm.sh

set -e

echo "🚀 Iniciando configuração da VM Azure..."
echo ""

# Cores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Atualizar sistema
echo -e "${BLUE}📦 Atualizando pacotes do sistema...${NC}"
sudo apt update
sudo apt upgrade -y

# Instalar utilitários básicos
echo -e "${BLUE}🛠️  Instalando utilitários básicos...${NC}"
sudo apt install -y \
    curl \
    wget \
    git \
    vim \
    htop \
    tree \
    unzip \
    ca-certificates \
    gnupg \
    lsb-release

# Instalar Docker
echo -e "${BLUE}🐳 Instalando Docker...${NC}"
# Remover versões antigas
sudo apt remove -y docker docker-engine docker.io containerd runc 2>/dev/null || true

# Adicionar chave GPG oficial do Docker
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Configurar repositório
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Instalar Docker Engine
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Adicionar usuário ao grupo docker
sudo usermod -aG docker $USER

echo -e "${YELLOW}⚠️  IMPORTANTE: Você precisa fazer logout e login novamente para usar Docker sem sudo${NC}"

# Instalar Docker Compose standalone (v2)
echo -e "${BLUE}🐙 Instalando Docker Compose...${NC}"
DOCKER_COMPOSE_VERSION=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep 'tag_name' | cut -d\" -f4)
sudo curl -L "https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Instalar Python 3 e pip
echo -e "${BLUE}🐍 Instalando Python 3 e pip...${NC}"
sudo apt install -y python3 python3-pip python3-venv

# Instalar Node.js (LTS via NodeSource)
echo -e "${BLUE}📗 Instalando Node.js LTS...${NC}"
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt install -y nodejs

# Configurar firewall básico
echo -e "${BLUE}🔥 Configurando firewall (ufw)...${NC}"
sudo apt install -y ufw
sudo ufw --force enable
sudo ufw allow 22/tcp  # SSH
echo -e "${YELLOW}Firewall configurado. Portas abertas: 22 (SSH)${NC}"
echo -e "${YELLOW}Para abrir mais portas: sudo ufw allow PORTA${NC}"

# Criar estrutura de pastas úteis
echo -e "${BLUE}📁 Criando estrutura de pastas...${NC}"
mkdir -p ~/projects
mkdir -p ~/backups
mkdir -p ~/scripts

# Criar arquivo de informações da VM
cat > ~/vm-info.txt << EOF
===========================================
   INFORMAÇÕES DA VM AZURE
===========================================

Hostname: $(hostname)
IP Interno: $(hostname -I | awk '{print $1}')
IP Externo: $(curl -s ifconfig.me)
Sistema: $(lsb_release -d | cut -f2)
Kernel: $(uname -r)

Configuração:
- CPUs: $(nproc)
- RAM: $(free -h | awk '/^Mem:/ {print $2}')
- Disco: $(df -h / | awk 'NR==2 {print $2}')

Ferramentas Instaladas:
- Docker: $(docker --version 2>/dev/null || echo "Faça logout/login para usar")
- Docker Compose: $(docker-compose --version)
- Python: $(python3 --version)
- Node.js: $(node --version)
- npm: $(npm --version)
- Git: $(git --version)

Data de Setup: $(date)
===========================================

Para ver este arquivo novamente: cat ~/vm-info.txt
EOF

# Exibir informações
echo ""
echo -e "${GREEN}✅ Setup concluído com sucesso!${NC}"
echo ""
cat ~/vm-info.txt
echo ""
echo -e "${YELLOW}🔄 PRÓXIMOS PASSOS:${NC}"
echo "1. Faça logout e login novamente: exit"
echo "2. Reconecte: ssh -i sua-chave.pem azureuser@SEU-IP"
echo "3. Teste o Docker: docker run hello-world"
echo "4. Seus projetos: cd ~/projects"
echo ""
echo -e "${GREEN}🎉 Sua VM está pronta para uso!${NC}"
