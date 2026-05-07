# 🖥️ Azure Virtual Machine - Exercício Prático

Aprenda a criar e gerenciar uma Máquina Virtual Linux (Ubuntu) no Azure.

## 📚 O que você vai aprender

- Criar uma VM Ubuntu no Azure Portal
- Conectar via SSH
- Executar comandos Linux básicos
- Instalar aplicações na VM
- Gerenciar a VM (start, stop, delete)
- (Opcional) Criar VM via Azure CLI

---

## 🎯 Parte 1: Criar a VM no Portal Azure

### Passo 1: Acessar o Portal

**1. Entre no Portal do Azure:**
```
https://portal.azure.com
```

**2. No menu lateral ou na barra de busca, procure por:**
```
Virtual Machines
```

**3. Clique em "+ Create" (Criar) → "Azure virtual machine"**

---

### Passo 2: Configurações Básicas (Basics)

#### **Aba: Basics**

| Campo | Valor | Explicação |
|-------|-------|------------|
| **Subscription** | (sua assinatura) | Fornecida pelo instrutor |
| **Resource group** | `rg-aluno-SEUNOME` | Crie um novo ou use existente |
| **Virtual machine name** | `vm-aluno-SEUNOME` | Ex: `vm-aluno-joao` |
| **Region** | `Brazil South` | Mais próximo = menor latência |
| **Availability options** | `No infrastructure redundancy required` | Economizar custos |
| **Security type** | `Standard` | Padrão para aprendizado |
| **Image** | `Ubuntu Server 22.04 LTS - x64 Gen2` | Sistema operacional |
| **VM architecture** | `x64` | Arquitetura do processador |
| **Size** | `Standard_B1s` | **IMPORTANTE: 1 vCPU, 1 GB RAM** |

⚠️ **ATENÇÃO ao Size:**
- Clique em **"See all sizes"**
- Procure por **B1s** na busca
- Selecione **Standard_B1s** (1 vCPU, 1 GiB memory)
- Este é o tamanho mais barato (~R$ 30/mês se ficar ligada 24/7)

#### **Administrator Account**

| Campo | Valor | Explicação |
|-------|-------|------------|
| **Authentication type** | `SSH public key` | Mais seguro que senha |
| **Username** | `azureuser` | Usuário padrão (pode mudar) |
| **SSH public key source** | `Generate new key pair` | Azure cria a chave para você |
| **Key pair name** | `vm-aluno-SEUNOME_key` | Nome da sua chave SSH |

💡 **O que é SSH?** É um protocolo seguro para conectar remotamente à VM via terminal.

#### **Inbound Port Rules**

| Campo | Valor | Explicação |
|-------|-------|------------|
| **Public inbound ports** | `Allow selected ports` | Permitir conexão SSH |
| **Select inbound ports** | ✅ `SSH (22)` | Porta 22 para SSH |

⚠️ **Segurança:** Apenas SSH por enquanto. Depois podemos abrir HTTP (80) se necessário.

**4. Clique em "Next: Disks >"**

---

### Passo 3: Configurar o Disco (Disks)

#### **Aba: Disks**

| Campo | Valor | Explicação |
|-------|-------|------------|
| **OS disk size** | `Image default (30 GiB)` | Tamanho padrão |
| **OS disk type** | `Standard SSD (locally-redundant storage)` | Barato e rápido o suficiente |
| **Delete with VM** | ✅ Marcado | Deleta o disco junto com a VM |
| **Encryption type** | `(Default) Encryption at-rest...` | Padrão |

💡 **Standard SSD vs Premium:** Standard é muito mais barato e suficiente para aprendizado.

**Clique em "Next: Networking >"**

---

### Passo 4: Configurar a Rede (Networking)

#### **Aba: Networking**

O Azure cria automaticamente:
- Virtual Network (VNet)
- Subnet
- Public IP
- Network Security Group (NSG)

**Deixe tudo no padrão, mas verifique:**

| Campo | Valor |
|-------|-------|
| **Virtual network** | `(new) vm-aluno-SEUNOME-vnet` |
| **Subnet** | `(new) default (10.0.0.0/24)` |
| **Public IP** | `(new) vm-aluno-SEUNOME-ip` |
| **NIC network security group** | `Basic` |
| **Public inbound ports** | `Allow selected ports` |
| **Select inbound ports** | ✅ SSH (22) |

**Delete public IP and NIC when VM is deleted:**
- ✅ Marque ambas as opções (para limpar tudo ao deletar)

**Clique em "Next: Management >"**

---

### Passo 5: Gerenciamento (Management)

#### **Aba: Management**

**Deixe tudo no padrão, mas observe:**

| Campo | Valor | Observação |
|-------|-------|------------|
| **Enable auto-shutdown** | ✅ MARQUE ISSO! | **Muito importante para economizar!** |
| **Shutdown time** | `19:00:00` | Ajuste conforme necessário |
| **Time zone** | `(UTC-03:00) Brasília` | Seu fuso horário |
| **Notification before shutdown** | ✅ Opcional | Email antes de desligar |

💰 **IMPORTANTE:** Auto-shutdown economiza dinheiro! A VM só é cobrada quando está ligada.

**Clique em "Next: Monitoring >"**

---

### Passo 6: Monitoramento (Monitoring)

#### **Aba: Monitoring**

Para economizar, desabilite alguns recursos:

| Campo | Valor |
|-------|-------|
| **Boot diagnostics** | `Enabled with managed storage account` |
| **Enable OS guest diagnostics** | ❌ Desabilitado |

**Clique em "Review + create"**

---

### Passo 7: Revisar e Criar

**1. Revise todas as configurações**

Confira especialmente:
- ✅ Size: `Standard_B1s`
- ✅ Image: `Ubuntu Server 22.04 LTS`
- ✅ Auto-shutdown: Habilitado

**2. Veja o custo estimado:**
```
Estimated cost: ~R$ 0,04/hora (~R$ 30/mês se ficar ligada 24/7)
```

**3. Clique em "Create" (Criar)**

---

### Passo 8: Baixar a Chave SSH

🔑 **ATENÇÃO - PASSO CRÍTICO!**

Quando a VM começar a ser criada, aparecerá um popup:

```
Generate new key pair
Download private key and create resource
```

**1. Clique em "Download private key and create resource"**

**2. O arquivo `vm-aluno-SEUNOME_key.pem` será baixado**

**3. ⚠️ GUARDE ESTE ARQUIVO COM SEGURANÇA!**
   - Sem ele, você NÃO consegue acessar a VM
   - Se perder, terá que recriar a VM

**4. Aguarde 3-5 minutos** até a mensagem:
```
✅ Your deployment is complete
```

---

## 🔐 Parte 2: Conectar na VM via SSH

### Passo 1: Pegar o IP Público

**1. Vá até "Virtual Machines" no portal**

**2. Clique na sua VM (`vm-aluno-SEUNOME`)**

**3. Copie o "Public IP address"**
```
Exemplo: 20.206.123.45
```

---

### Passo 2: Preparar a Chave SSH

#### **No Linux/Mac:**

```bash
# 1. Mova a chave para a pasta .ssh
mkdir -p ~/.ssh
mv ~/Downloads/vm-aluno-SEUNOME_key.pem ~/.ssh/

# 2. Ajuste as permissões (obrigatório!)
chmod 400 ~/.ssh/vm-aluno-SEUNOME_key.pem
```

#### **No Windows:**

**Opção A - WSL (Windows Subsystem for Linux):**
```bash
# Abra o WSL e faça o mesmo que Linux/Mac acima
```

**Opção B - PowerShell nativo:**
```powershell
# Mova a chave para um lugar seguro
Move-Item -Path "$env:USERPROFILE\Downloads\vm-aluno-SEUNOME_key.pem" -Destination "$env:USERPROFILE\.ssh\"

# As permissões no Windows são ajustadas automaticamente
```

---

### Passo 3: Conectar via SSH

#### **No Linux/Mac/WSL:**

```bash
ssh -i ~/.ssh/vm-aluno-SEUNOME_key.pem azureuser@SEU-IP-PUBLICO
```

Exemplo real:
```bash
ssh -i ~/.ssh/vm-aluno-joao_key.pem azureuser@20.206.123.45
```

#### **No Windows PowerShell:**

```powershell
ssh -i $env:USERPROFILE\.ssh\vm-aluno-SEUNOME_key.pem azureuser@SEU-IP-PUBLICO
```

---

### Passo 4: Primeira Conexão

**1. Na primeira vez, aparecerá:**
```
The authenticity of host '20.206.123.45' can't be established.
Are you sure you want to continue connecting (yes/no)?
```

Digite: `yes`

**2. Você verá o prompt do Ubuntu:**
```
azureuser@vm-aluno-joao:~$
```

🎉 **Parabéns! Você está conectado na sua VM no Azure!**

---

## 💻 Parte 3: Comandos Básicos Linux

### Explorar a VM

```bash
# Ver informações do sistema
uname -a

# Ver quanto de memória tem
free -h

# Ver o espaço em disco
df -h

# Ver informações da CPU
lscpu

# Ver processos rodando
top
# (pressione 'q' para sair)

# Ver qual usuário você é
whoami

# Ver em qual diretório você está
pwd

# Listar arquivos
ls -la

# Ver o IP da VM
ip addr show
```

---

### Atualizar o Sistema

**Sempre faça isso primeiro em uma VM nova:**

```bash
# Atualizar a lista de pacotes
sudo apt update

# Fazer upgrade dos pacotes instalados
sudo apt upgrade -y

# Ver a versão do Ubuntu
lsb_release -a
```

💡 **sudo** = "super user do" - roda o comando como administrador

---

### Instalar Programas

#### **Exemplo 1: Instalar o Nginx (servidor web)**

```bash
# Instalar
sudo apt install nginx -y

# Verificar se está rodando
sudo systemctl status nginx

# Iniciar se não estiver rodando
sudo systemctl start nginx

# Habilitar para iniciar automaticamente
sudo systemctl enable nginx
```

**Para testar:**
1. No Portal Azure, vá na sua VM
2. Em "Networking" → "Add inbound port rule"
3. Adicione porta 80 (HTTP)
4. Acesse `http://SEU-IP-PUBLICO` no navegador
5. Deve aparecer a página "Welcome to nginx!"

---

#### **Exemplo 2: Instalar Docker**

```bash
# Instalar dependências
sudo apt install apt-transport-https ca-certificates curl software-properties-common -y

# Adicionar a chave GPG do Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Adicionar o repositório do Docker
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Atualizar e instalar
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io -y

# Adicionar seu usuário ao grupo docker (para não precisar de sudo)
sudo usermod -aG docker $USER

# Sair e entrar novamente para aplicar
exit
# (conecte novamente com o comando ssh)

# Testar
docker --version
docker run hello-world
```

---

#### **Exemplo 3: Instalar Python e pip**

```bash
# Instalar Python 3 e pip
sudo apt install python3 python3-pip -y

# Verificar versões
python3 --version
pip3 --version

# Instalar um pacote Python (exemplo)
pip3 install requests

# Criar um script Python simples
cat > hello.py << 'EOF'
#!/usr/bin/env python3
print("🎉 Hello from Azure VM!")
print("🐍 Python está funcionando!")
EOF

# Executar
python3 hello.py
```

---

### Transferir Arquivos

#### **Do seu computador → VM:**

```bash
# No seu computador (não na VM!)
scp -i ~/.ssh/vm-aluno-SEUNOME_key.pem arquivo.txt azureuser@SEU-IP:/home/azureuser/
```

#### **Da VM → seu computador:**

```bash
# No seu computador (não na VM!)
scp -i ~/.ssh/vm-aluno-SEUNOME_key.pem azureuser@SEU-IP:/home/azureuser/arquivo.txt ./
```

---

## 🛠️ Parte 4: Gerenciar a VM

### Via Portal Azure

**Iniciar (Start):**
1. Vá em "Virtual Machines"
2. Selecione sua VM
3. Clique em "Start" (▶️)

**Parar (Stop):**
1. Clique em "Stop" (⏹️)
2. **Status:** "Stopped (deallocated)" - **não é cobrado neste estado**

⚠️ **IMPORTANTE:** Sempre "Stop (deallocate)", não apenas "Stop"!

**Reiniciar (Restart):**
- Clique em "Restart" (🔄)

**Deletar (Delete):**
1. Clique em "Delete"
2. ✅ Marque todas as opções (delete disks, NICs, IPs)
3. Digite o nome da VM para confirmar
4. Clique em "Delete"

---

### Monitorar Custos

**1. Vá em "Cost Management + Billing"**

**2. Veja os gastos por:**
- Recurso (sua VM)
- Dia
- Mês

**3. Configure alertas:**
- "Budgets" → "Add"
- Defina um limite (ex: R$ 50/mês)
- Receba email se ultrapassar

---

## 📝 Exercícios Práticos

### Exercício 1: Primeira VM
1. ✅ Crie a VM B1s Ubuntu 22.04
2. ✅ Conecte via SSH
3. ✅ Rode `sudo apt update && sudo apt upgrade -y`
4. ✅ Crie um arquivo de texto: `echo "Olá Azure!" > teste.txt`
5. ✅ Tire um print do terminal conectado

### Exercício 2: Instalar Nginx
1. ✅ Instale o Nginx
2. ✅ Libere a porta 80 no NSG (Network Security Group)
3. ✅ Acesse `http://SEU-IP` e veja a página padrão
4. ✅ Edite a página: `sudo nano /var/www/html/index.nginx-debian.html`
5. ✅ Coloque seu nome e atualize a página

### Exercício 3: Hospedar um Site
1. ✅ Crie uma pasta: `mkdir ~/meu-site`
2. ✅ Crie um `index.html` simples
3. ✅ Copie para `/var/www/html/`: `sudo cp ~/meu-site/index.html /var/www/html/`
4. ✅ Acesse no navegador e compartilhe com a turma!

### Exercício 4: Auto-Shutdown
1. ✅ Configure auto-shutdown para 18:00
2. ✅ Aguarde e veja se a VM desliga sozinha
3. ✅ Ligue novamente manualmente

### Exercício 5: Transferência de Arquivos
1. ✅ Crie um arquivo no seu computador
2. ✅ Use `scp` para enviar para a VM
3. ✅ Baixe um arquivo da VM para seu computador

### Exercício 6: Desafio - Deploy Docker
1. ✅ Instale Docker na VM
2. ✅ Rode um container: `docker run -d -p 8080:80 nginx`
3. ✅ Libere a porta 8080 no NSG
4. ✅ Acesse `http://SEU-IP:8080`

---

## 🚀 Parte 5: Via Azure CLI (Avançado/Opcional)

### Instalar Azure CLI

#### **Linux/WSL:**
```bash
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

#### **Mac:**
```bash
brew install azure-cli
```

#### **Windows:**
Baixe o instalador em: https://aka.ms/installazurecliwindows

---

### Comandos para Criar a VM

```bash
# 1. Fazer login
az login

# 2. Criar Resource Group
az group create \
  --name rg-aluno-SEUNOME \
  --location brazilsouth

# 3. Criar a VM
az vm create \
  --resource-group rg-aluno-SEUNOME \
  --name vm-aluno-SEUNOME \
  --image Ubuntu2204 \
  --size Standard_B1s \
  --admin-username azureuser \
  --generate-ssh-keys \
  --public-ip-sku Standard

# 4. Abrir porta 22 (SSH)
az vm open-port \
  --resource-group rg-aluno-SEUNOME \
  --name vm-aluno-SEUNOME \
  --port 22

# 5. Pegar o IP público
az vm list-ip-addresses \
  --resource-group rg-aluno-SEUNOME \
  --name vm-aluno-SEUNOME \
  --output table

# 6. Conectar
ssh azureuser@SEU-IP-PUBLICO
```

---

### Comandos Úteis da CLI

```bash
# Listar todas as VMs
az vm list --output table

# Iniciar VM
az vm start \
  --resource-group rg-aluno-SEUNOME \
  --name vm-aluno-SEUNOME

# Parar VM (deallocate = não cobra)
az vm deallocate \
  --resource-group rg-aluno-SEUNOME \
  --name vm-aluno-SEUNOME

# Reiniciar VM
az vm restart \
  --resource-group rg-aluno-SEUNOME \
  --name vm-aluno-SEUNOME

# Ver status
az vm get-instance-view \
  --resource-group rg-aluno-SEUNOME \
  --name vm-aluno-SEUNOME \
  --query instanceView.statuses[1] \
  --output table

# Deletar tudo (VM + recursos)
az group delete \
  --name rg-aluno-SEUNOME \
  --yes \
  --no-wait
```

---

## 💰 Gerenciamento de Custos

### Quanto Custa uma B1s?

**Preços aproximados (região Brazil South):**

| Cenário | Custo |
|---------|-------|
| **Ligada 24/7 por 1 mês** | ~R$ 30-35/mês |
| **Ligada 8h/dia (dias úteis)** | ~R$ 8-10/mês |
| **Ligada 1h/dia** | ~R$ 1-2/mês |
| **Desligada (deallocated)** | R$ 0,00 (só paga disco: ~R$ 1/mês) |

💡 **Dica:** Use auto-shutdown e lembre de desligar quando não estiver usando!

---

### Checklist para Economizar

- ✅ Sempre use **auto-shutdown**
- ✅ Desligue a VM quando terminar de usar
- ✅ Delete recursos não utilizados
- ✅ Use o tamanho **B1s** (o mais barato)
- ✅ Configure alertas de custo
- ✅ Delete snapshots e discos órfãos

---

## 🆘 Problemas Comuns

### Não consigo conectar via SSH

**Erro: "Connection refused"**
→ Verifique:
1. A VM está ligada? (Status = "Running")
2. Porta 22 está aberta no NSG?
3. O IP está correto?

**Erro: "Permission denied (publickey)"**
→ Verifique:
1. Está usando a chave correta? (`-i caminho/para/chave.pem`)
2. As permissões da chave estão corretas? (`chmod 400 chave.pem`)
3. O username está correto? (deve ser `azureuser`)

**Erro: "Host key verification failed"**
```bash
# Se recriou a VM com o mesmo IP, limpe o known_hosts:
ssh-keygen -R SEU-IP-PUBLICO
```

---

### VM está lenta

B1s tem recursos limitados (1 vCPU, 1 GB RAM):
- ✅ Normal para tarefas leves
- ❌ Não recomendado para compilação pesada
- ❌ Não recomendado para bancos de dados grandes
- ✅ Bom para aprendizado, sites estáticos, APIs simples

**Dica:** Use `htop` para ver uso de recursos:
```bash
sudo apt install htop -y
htop
```

---

### Esqueci a chave SSH

❌ **Não tem como recuperar!**

**Soluções:**
1. No portal, vá em "Reset password"
2. Ou recrie a VM (lembre de fazer backup dos dados antes)

---

### Custos inesperados

**Verifique:**
1. A VM está deallocated quando desligada?
2. Tem discos órfãos? (Vá em "Disks" e delete os não usados)
3. Tem IPs públicos não usados? (Delete em "Public IP addresses")
4. Tem snapshots antigos? (Delete em "Snapshots")

---

## 📚 Próximos Passos

Depois de dominar o básico, você pode:

1. **Hospedar aplicações:**
   - Site com Nginx
   - API com Node.js/Python
   - Banco de dados PostgreSQL/MySQL

2. **Configurar domínio:**
   - Comprar domínio (ex: .com.br)
   - Apontar DNS para o IP da VM
   - Configurar HTTPS com Let's Encrypt

3. **CI/CD:**
   - Deploy automático com GitHub Actions
   - Pipeline Azure DevOps

4. **Load Balancer:**
   - Criar múltiplas VMs
   - Balancear carga entre elas

5. **Containers:**
   - Migrar para Azure Container Instances
   - Ou Azure Kubernetes Service (AKS)

---

## 🔗 Recursos Adicionais

- [Documentação Oficial - Azure VMs](https://docs.microsoft.com/azure/virtual-machines/)
- [Tutorial Interativo Microsoft Learn](https://docs.microsoft.com/learn/modules/create-linux-virtual-machine-in-azure/)
- [Preços das VMs](https://azure.microsoft.com/pricing/details/virtual-machines/linux/)
- [Calculadora de Custos Azure](https://azure.microsoft.com/pricing/calculator/)
- [Linux Command Line Basics](https://ubuntu.com/tutorials/command-line-for-beginners)

---

## 📊 Resumo dos Comandos SSH

```bash
# Conectar
ssh -i ~/.ssh/chave.pem azureuser@SEU-IP

# Transferir arquivo (local → VM)
scp -i ~/.ssh/chave.pem arquivo.txt azureuser@SEU-IP:/home/azureuser/

# Transferir arquivo (VM → local)
scp -i ~/.ssh/chave.pem azureuser@SEU-IP:/home/azureuser/arquivo.txt ./

# Desconectar
exit
```

---

**Dúvidas?** Pergunte ao seu instrutor ou na comunidade! 🙋

**Lembre-se:** Sempre desligue a VM quando terminar! 💰
