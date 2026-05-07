# 🎓 ETEC Bentão - Exercícios Práticos de Cloud & DevOps

Repositório de exercícios práticos para alunos aprenderem sobre infraestrutura em nuvem, containers, e desenvolvimento moderno.

## 📚 Conteúdo do Curso

### ☁️ Introdução a Cloud Computing
**Aprenda os conceitos fundamentais de computação em nuvem**

- ✅ O que é Cloud e por que usar
- ✅ Tipos de serviços: IaaS, PaaS, SaaS
- ✅ Principais provedores (Azure, Google Cloud, AWS)
- ✅ Conceitos de custo e segurança

👉 [Ver conceitos básicos](./docs/conceitos-basicos-cloud.md)

👉 [Ver guia completo](./docs/introducao-cloud.md) (opcional, aprofundado)

---

## 🛠️ Exercícios Práticos

### 🐳 Docker Compose
**Aprenda a orquestrar containers Docker**

Um exercício prático com uma aplicação Node.js + Redis rodando em containers.

- ✅ Containers comunicando entre si
- ✅ Persistência de dados com Redis
- ✅ Cada aluno roda em sua própria porta (sem conflitos)
- ✅ Logs e debugging

👉 [Ver instruções completas](./docker-compose/README.md)

---

### ☁️ Azure Storage Account
**Hospede arquivos e sites na nuvem da Microsoft**

Aprenda a usar o Azure Storage para armazenar arquivos e hospedar sites estáticos.

**Parte 1 - Armazenamento de Arquivos:**
- ✅ Criar um Storage Account
- ✅ Upload e download de arquivos (Blobs)
- ✅ Gerenciar containers
- ✅ Scripts Python para automação

**Parte 2 - Hospedagem de Sites:**
- ✅ Hospedar um site HTML na internet
- ✅ Static Website Hosting
- ✅ Personalizar e publicar seu próprio site

👉 [Ver instruções completas](./azure/storage/README.md)

👉 [Guia de hospedagem de sites](./azure/storage/website/README.md)

---

### 🖥️ Azure Virtual Machine
**Crie e gerencie máquinas virtuais Linux na nuvem**

Aprenda a criar uma VM Ubuntu no Azure e hospedar aplicações.

- ✅ Criar VM Ubuntu (tamanho B1s)
- ✅ Conectar via SSH
- ✅ Instalar Docker e outras ferramentas
- ✅ Hospedar aplicações web
- ✅ Gerenciar custos e recursos

👉 [Ver instruções completas](./azure/vm/README.md)

---

### 🌐 Azure App Service
**Hospede aplicações web sem gerenciar servidores (PaaS)**

Aprenda a fazer deploy de aplicações Node.js/Python na nuvem.

- ✅ Criar App Service (F1 Free ou B1 Basic)
- ✅ Deploy via Git, VS Code ou CLI
- ✅ Variáveis de ambiente e configurações
- ✅ SSL/HTTPS automático
- ✅ Diferença entre PaaS e IaaS

👉 [Ver instruções completas](./azure/app-service/README.md)

---

### 🔐 Azure Key Vault
**Guarde senhas e segredos de forma segura**

Aprenda a armazenar e gerenciar secrets, chaves de API e certificados.

- ✅ Criar Key Vault
- ✅ Armazenar secrets (senhas, API keys)
- ✅ Usar secrets em aplicações Node.js/Python
- ✅ Controlar acessos com policies
- ✅ Boas práticas de segurança

👉 [Ver instruções completas](./azure/key-vault/README.md)

---

### 📊 Application Insights + Log Analytics
**Monitore e analise suas aplicações**

Aprenda a usar ferramentas de monitoramento do Azure.

- ✅ Habilitar Application Insights
- ✅ Ver métricas de performance
- ✅ Analisar logs com queries KQL
- ✅ Criar alertas e dashboards
- ✅ Detectar problemas antes dos usuários

👉 [Ver instruções completas](./azure/monitoring/README.md)

---

### 📋 Azure Policy
**Controle de custos e governança**

Configure regras para bloquear recursos caros e garantir conformidade.

- ✅ Criar e aplicar policies
- ✅ Bloquear VMs grandes
- ✅ Forçar uso de regiões brasileiras
- ✅ Controlar custos automaticamente
- ✅ Monitorar compliance

👉 [Ver instruções completas](./azure/policy/README.md)

⚠️ **Para instrutores:** Aplique a policy ANTES de liberar acesso aos alunos!

---

### 🔐 Azure Entra ID (em breve)
**Gerenciamento de identidade e acesso**

- Convites de usuários
- Grupos e permissões
- Autenticação e autorização

👉 Ver pasta `azure/entra/`

---

## 🚀 Como Começar

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/toolbox-playground/etec-bentao.git
   cd etec-bentao
   ```

2. **Escolha um exercício:**
   - Para Docker: vá para a pasta raiz e siga o [README de Docker](./README-docker.md)
   - Para Azure Storage: vá para [`azure/storage/`](./azure/storage/)

3. **Siga as instruções passo a passo**

4. **Tire dúvidas na nossa comunidade!** 👇

---

## 💬 Comunidade & Suporte

Junte-se à nossa comunidade para tirar dúvidas, compartilhar projetos e aprender junto!

### 📱 Participe do nosso WhatsApp
👉 **[Entrar na comunidade](https://chat.whatsapp.com/JLKp1OqAOa03Nc1iN8F1kb)**

### 🌐 Nossas Redes Sociais

- 💼 **LinkedIn:** [ToolBox Technology](https://www.linkedin.com/company/toolboxtech/)
- 🌍 **Site:** [tbxtech.com.br](https://tbxtech.com.br/)
- 🎥 **YouTube:** [@ToolboxTechnology](https://www.youtube.com/@ToolboxTechnology)
- 📸 **Instagram:** [@toolboxtechnology](https://www.instagram.com/toolboxtechnology/)
- 💬 **Discord:** [Servidor Discord](https://discord.gg/vGfZj7QBwC)

---

## 🛠️ Pré-requisitos

### Para Docker:
- Docker e Docker Compose instalados
- Acesso a uma VM ou servidor Linux
- Porta atribuída pelo instrutor

### Para Azure:
- Conta no Azure (será fornecida pelo instrutor)
- Python 3.8+ instalado (para scripts)
- Navegador web para acessar o Portal Azure

---

## 📖 Estrutura do Repositório

```
etec-bentao/
├── README.md                    # Este arquivo
├── .gitignore                   # Arquivos a ignorar no Git
├── docker-compose.yml           # Exercício de Docker Compose
├── Dockerfile
├── app.js
├── .env.example
│
├── docs/                        # Documentação e teoria
│   ├── conceitos-basicos-cloud.md   # Conceitos essenciais (30-45min)
│   └── introducao-cloud.md          # Guia completo (opcional)
│
└── azure/                       # Exercícios do Azure
    ├── storage/                 # Azure Storage Account
    │   ├── README.md           # Guia de Storage
    │   ├── upload_file.py      # Scripts Python
    │   ├── download_file.py
    │   ├── list_files.py
    │   ├── create_container.py
    │   ├── test_setup.py
    │   ├── upload_website.py
    │   ├── requirements.txt
    │   ├── .env.example
    │   │
    │   └── website/            # Site estático para hospedar
    │       ├── README.md       # Guia de Static Website
    │       ├── index.html
    │       ├── style.css
    │       └── script.js
    │
    ├── vm/                      # Azure Virtual Machines
    │   ├── README.md           # Guia completo de VMs
    │   ├── setup-vm.sh         # Script de setup automático
    │   └── deploy-docker-app.sh # Deploy do app Docker na VM
    │
    ├── app-service/            # Azure App Service (PaaS)
    │   └── README.md           # Guia de App Service
    │
    ├── key-vault/              # Azure Key Vault
    │   └── README.md           # Guia de segredos e secrets
    │
    ├── monitoring/             # Application Insights + Log Analytics
    │   └── README.md           # Guia de monitoramento
    │
    ├── policy/                 # Azure Policy
    │   ├── README.md           # Guia de governança
    │   └── policy.json         # Policy de controle de custos
    │
    └── entra/                  # Azure Entra ID (em breve)
```

---

## 🎯 Objetivos de Aprendizado

Ao completar esses exercícios, você será capaz de:

### **Fundamentos**
- ☁️ **Entender conceitos de Cloud** - IaaS, PaaS, SaaS
- 🐳 **Containerizar aplicações** com Docker
- 💰 **Gerenciar custos** em cloud

### **Azure - IaaS (Infrastructure)**
- 🖥️ **Criar e gerenciar VMs** Linux no Azure
- 📦 **Armazenar arquivos** com Storage Account
- 🌐 **Hospedar sites estáticos** na internet
- 🔐 **Conectar via SSH** e administrar servidores

### **Azure - PaaS (Platform)**
- 🚀 **Deploy de aplicações** com App Service
- 🔑 **Gerenciar segredos** com Key Vault
- 📊 **Monitorar aplicações** com Application Insights
- 📝 **Analisar logs** com Log Analytics

### **Azure - Governança**
- 📋 **Aplicar policies** de governança
- 💸 **Controlar custos** automaticamente
- 🔒 **Garantir conformidade** (LGPD, regiões)
- 🚨 **Criar alertas** de performance e custo

### **Habilidades Práticas**
- 🔧 **Automatizar tarefas** com scripts Python/Bash
- 📊 **Debugar e resolver problemas** em produção
- 🤝 **Trabalhar em equipe** com ferramentas modernas
- 🎓 **Aprender continuamente** novos recursos

---

## 👨‍🏫 Para Instrutores

### ⚠️ IMPORTANTE: Aplicar Azure Policy ANTES da Aula!

**Para controlar custos e evitar surpresas:**

```bash
# 1. Clone o repositório
git clone https://github.com/toolbox-playground/etec-bentao.git
cd etec-bentao

# 2. Executar script de aplicação da policy
bash azure/policy/apply-policy.sh
```

Ou siga o guia completo: **[Setup do Instrutor](./docs/setup-instrutor.md)**

---

### Preparação do Ambiente

**Resource Group:**
- ✅ Já criado: `etec-bentao`
- 📋 Aplicar policy de controle de custos (ver acima)
- 💰 Configurar budget alerts (ver [guia](./docs/setup-instrutor.md))

**Acesso dos Alunos:**
- **Opção A:** Conta compartilhada (mais simples)
- **Opção B:** Conta individual por aluno
- Ver detalhes em: [Setup do Instrutor](./docs/setup-instrutor.md)

**Docker Compose:**
1. Provisione uma VM Linux com Docker instalado
2. Atribua portas para cada aluno (8001, 8002, 8003...)
3. Compartilhe o IP da VM e as portas

### Cronograma Sugerido

#### **Opção 1: Curso Básico (4 horas)**

**Módulo 1: Introdução (1h)**
- Conceitos de Cloud Computing (30min) - [Ver material](./docs/conceitos-basicos-cloud.md)
- Apresentação do Azure Portal (15min)
- Criar conta e explorar interface (15min)

**Módulo 2: Azure Storage (1h30)**
- Criar Storage Account (15min)
- Upload/Download de arquivos (30min)
- Hospedar site estático (45min)

**Módulo 3: Azure Virtual Machine (1h)**
- Criar VM Ubuntu B1s (20min)
- Conectar via SSH (15min)
- Instalar Docker (25min)

**Wrap-up (30min)**
- Limpeza de recursos
- Melhores práticas
- Próximos passos

---

#### **Opção 2: Curso Completo (8-12 horas)**

**Dia 1 - Fundamentos (4h)**
- Conceitos de Cloud (1h)
- Azure Storage Account (1h30)
- Azure Virtual Machine (1h30)

**Dia 2 - PaaS e Segurança (4h)**
- Azure App Service (1h30)
- Azure Key Vault (1h)
- Azure Policy (controle de custos) (1h)
- Application Insights (30min)

**Dia 3 - Projeto Final (4h)**
- Projeto integrado: App completo com todos os recursos
- Apresentações dos alunos
- Feedback e certificados

---

#### **Opção 3: Workshop Rápido (2 horas)**

**Ideal para demonstração**

- Conceitos de Cloud (20min)
- Demo: Hospedar site no Storage (40min)
- Demo: Criar VM e rodar Docker (40min)
- Q&A e próximos passos (20min)

---

## 🤝 Contribuindo

Encontrou um erro? Tem uma sugestão de melhoria?

1. Abra uma [Issue](https://github.com/toolbox-playground/etec-bentao/issues)
2. Ou faça um Pull Request!

---

## 📝 Licença

Este projeto é open-source e está disponível sob a licença MIT.

---

## 🙋 Perguntas Frequentes

### Posso usar este material em outras escolas?
Sim! O material é totalmente gratuito e aberto. Sinta-se à vontade para adaptar para sua realidade.

### Preciso pagar pelo Azure?
Para os exercícios básicos, o custo é mínimo (centavos). Recomendamos que a escola/instrutor forneça uma assinatura, ou use o Azure for Students (gratuito).

### E se eu não tiver acesso a uma VM para Docker?
Você pode usar Docker Desktop no Windows/Mac, ou plataformas gratuitas como GitHub Codespaces.

### Como deletar os recursos do Azure depois?
Siga as instruções de "Limpeza" em cada exercício. Geralmente é só deletar o Resource Group.

---

## 🎉 Showcase de Alunos

Completou os exercícios? Compartilhe seu site hospedado ou projeto!

- Envie o link no grupo do WhatsApp
- Ou abra um Pull Request adicionando na seção de showcase

---

**Feito com 💙 pela equipe [ToolBox Technology](https://tbxtech.com.br/)**

**Bons estudos! 🚀**
