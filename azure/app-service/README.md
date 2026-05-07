# 🌐 Azure App Service - Exercício Prático

Hospede aplicações web sem se preocupar com servidores!

## 📚 O que você vai aprender

- Criar um App Service (PaaS)
- Fazer deploy de aplicação Node.js
- Configurar variáveis de ambiente
- Usar deployment slots (staging/production)
- Diferença entre App Service e VM

---

## 🎯 O que é App Service?

**Definição:**
É uma plataforma PaaS (Platform as a Service) para hospedar aplicações web, APIs e backends móveis.

**Diferença de VM:**
- ❌ **VM (IaaS):** Você gerencia sistema operacional, runtime, segurança
- ✅ **App Service (PaaS):** Você só faz deploy do código!

**Linguagens suportadas:**
- Node.js, Python, .NET, Java, PHP, Ruby

---

## 💰 Níveis de Preço (SKUs)

| Tier | Custo | Recursos | Quando usar |
|------|-------|----------|-------------|
| **F1 (Free)** | Grátis! | 1GB RAM, 60min/dia CPU | Testes, aprendizado |
| **B1 (Basic)** | ~R$ 50/mês | 1.75GB RAM, SSL customizado | Apps pequenos, produção básica |
| **S1 (Standard)** | ~R$ 250/mês | 1.75GB RAM, auto-scale, slots | Produção média |
| **P1 (Premium)** | ~R$ 500/mês | 3.5GB RAM, mais performance | Produção crítica |

⚠️ **Para este curso:** Usaremos **F1 (Free)** ou **B1 (Basic)**

---

## 🚀 Parte 1: Criar App Service no Portal

### Passo 1: Criar App Service

**1. Acesse o Portal Azure:**
```
https://portal.azure.com
```

**2. Pesquise por "App Services"**

**3. Clique em "+ Create"**

---

### Passo 2: Configurações Básicas

#### **Aba: Basics**

| Campo | Valor | Explicação |
|-------|-------|------------|
| **Subscription** | Sua assinatura | Fornecida pelo instrutor |
| **Resource group** | `rg-aluno-SEUNOME` | Use existente ou crie novo |
| **Name** | `app-aluno-SEUNOME` | Ex: `app-aluno-joao` (será `app-aluno-joao.azurewebsites.net`) |
| **Publish** | `Code` | Vamos fazer deploy de código |
| **Runtime stack** | `Node 20 LTS` | Versão do Node.js |
| **Operating System** | `Linux` | Mais barato que Windows |
| **Region** | `Brazil South` | Mais próximo dos usuários |

---

#### **App Service Plan**

| Campo | Valor |
|-------|-------|
| **Linux Plan** | Crie novo: `plan-aluno-SEUNOME` |
| **Pricing plan** | Clique em "Explore pricing plans" |
| | Escolha **F1 (Free)** ou **B1 (Basic)** |

💡 **Dica:** F1 é grátis mas tem limites; B1 é barato e sem limites diários.

**4. Clique em "Review + create"**

**5. Clique em "Create"**

**6. Aguarde 1-2 minutos**

---

## 📦 Parte 2: Deploy da Aplicação

### Opção A: Deploy via Portal (Mais Fácil)

#### 1. Criar aplicação simples

Crie uma pasta local com estes arquivos:

**`package.json`:**
```json
{
  "name": "meu-app-azure",
  "version": "1.0.0",
  "description": "Meu primeiro app no Azure",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "express": "^4.18.0"
  },
  "engines": {
    "node": ">=18.0.0"
  }
}
```

**`server.js`:**
```javascript
const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

// Página inicial
app.get('/', (req, res) => {
  res.send(`
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Meu App Azure</title>
      <style>
        body {
          font-family: Arial, sans-serif;
          background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
          color: white;
          text-align: center;
          padding: 50px;
        }
        .container {
          background: rgba(255,255,255,0.1);
          padding: 40px;
          border-radius: 20px;
          max-width: 600px;
          margin: 0 auto;
        }
        h1 { font-size: 3em; margin: 0; }
        p { font-size: 1.2em; }
      </style>
    </head>
    <body>
      <div class="container">
        <h1>🚀 Olá do Azure!</h1>
        <p>Meu primeiro app no Azure App Service</p>
        <p>Criado por: <strong>[SEU NOME]</strong></p>
        <p>Servidor rodando na porta ${port}</p>
        <p>Hora do servidor: ${new Date().toLocaleString('pt-BR')}</p>
      </div>
    </body>
    </html>
  `);
});

// API de exemplo
app.get('/api/info', (req, res) => {
  res.json({
    app: 'Meu App Azure',
    versao: '1.0.0',
    ambiente: process.env.NODE_ENV || 'development',
    timestamp: new Date().toISOString()
  });
});

app.listen(port, () => {
  console.log(`Servidor rodando na porta ${port}`);
});
```

**`.gitignore`:**
```
node_modules/
.env
*.log
```

#### 2. Fazer Deploy

**Via Git (recomendado):**

```bash
# 1. Inicializar Git na pasta do projeto
cd meu-app
git init
git add .
git commit -m "Initial commit"

# 2. No Portal Azure, vá no seu App Service
# 3. Vá em "Deployment Center"
# 4. Escolha "Local Git"
# 5. Copie a Git URL fornecida
# 6. No terminal:

git remote add azure <GIT-URL-DO-AZURE>
git push azure main

# 7. Digite as credenciais quando solicitado
```

**Via VS Code (mais fácil):**

1. Instale a extensão "Azure App Service"
2. Clique com botão direito na pasta do projeto
3. "Deploy to Web App"
4. Selecione seu App Service

---

### Opção B: Deploy via Azure CLI

```bash
# 1. Fazer login
az login

# 2. Criar Resource Group (se não tiver)
az group create --name rg-aluno-SEUNOME --location brazilsouth

# 3. Criar App Service Plan
az appservice plan create \
  --name plan-aluno-SEUNOME \
  --resource-group rg-aluno-SEUNOME \
  --sku F1 \
  --is-linux

# 4. Criar Web App
az webapp create \
  --name app-aluno-SEUNOME \
  --resource-group rg-aluno-SEUNOME \
  --plan plan-aluno-SEUNOME \
  --runtime "NODE:20-lts"

# 5. Deploy do código (na pasta do projeto)
cd meu-app
zip -r app.zip .
az webapp deploy \
  --resource-group rg-aluno-SEUNOME \
  --name app-aluno-SEUNOME \
  --src-path app.zip \
  --type zip

# 6. Ver logs
az webapp log tail \
  --resource-group rg-aluno-SEUNOME \
  --name app-aluno-SEUNOME
```

---

## 🔧 Parte 3: Configurações

### Variáveis de Ambiente

**Via Portal:**
1. Vá no seu App Service
2. "Configuration" → "Application settings"
3. Clique em "+ New application setting"
4. Adicione:
   - `NODE_ENV` = `production`
   - `CUSTOM_MESSAGE` = `Hello Azure!`
5. Clique em "Save"

**Via CLI:**
```bash
az webapp config appsettings set \
  --resource-group rg-aluno-SEUNOME \
  --name app-aluno-SEUNOME \
  --settings NODE_ENV=production CUSTOM_MESSAGE="Hello Azure!"
```

**Usar no código:**
```javascript
const message = process.env.CUSTOM_MESSAGE || 'Default message';
console.log(message);
```

---

### Domínio Customizado

**Seu app vem com:**
```
https://app-aluno-SEUNOME.azurewebsites.net
```

**Para usar domínio próprio (ex: `www.seunome.com.br`):**
1. Vá em "Custom domains"
2. Clique em "Add custom domain"
3. Siga as instruções para configurar DNS
4. **Importante:** Precisa do tier B1 ou superior!

---

### SSL/HTTPS

**Certificado gratuito:**
1. Após adicionar domínio customizado
2. Vá em "TLS/SSL settings"
3. "Private Key Certificates (.pfx)"
4. "Create App Service Managed Certificate" (grátis!)

**Let's Encrypt (alternativa):**
- Use a extensão do App Service

---

## 📊 Parte 4: Monitoramento

### Ver Logs em Tempo Real

**Via Portal:**
1. Vá no App Service
2. "Log stream"
3. Veja os logs ao vivo!

**Via CLI:**
```bash
az webapp log tail \
  --resource-group rg-aluno-SEUNOME \
  --name app-aluno-SEUNOME
```

---

### Métricas

**No Portal:**
1. Vá em "Metrics"
2. Veja:
   - CPU %
   - Memória
   - Requisições HTTP
   - Tempo de resposta

---

## 🎯 Parte 5: App Service vs VM

| Aspecto | App Service (PaaS) | Virtual Machine (IaaS) |
|---------|-------------------|------------------------|
| **Setup** | Minutos | 5-10 minutos + configuração |
| **Você gerencia** | Apenas código | SO, runtime, segurança, tudo |
| **Escalabilidade** | Automática (built-in) | Manual (você configura) |
| **Custo** | Por tier | Por hora de VM |
| **SSL/HTTPS** | Grátis e fácil | Você configura (Let's Encrypt) |
| **Deploy** | Git, VS Code, CLI | SSH + configuração manual |
| **Ideal para** | Apps web, APIs | Qualquer coisa, controle total |

**Quando usar App Service:**
- ✅ App web padrão (Node, Python, .NET)
- ✅ Quer focar no código, não em infraestrutura
- ✅ Precisa de SSL fácil
- ✅ Quer auto-scale

**Quando usar VM:**
- ✅ Precisa de controle total
- ✅ Linguagem/runtime não suportado
- ✅ Software específico precisa ser instalado
- ✅ Migração de servidor físico

---

## 📝 Exercícios Práticos

### Exercício 1: Primeiro Deploy
1. ✅ Crie um App Service F1
2. ✅ Faça deploy do código de exemplo
3. ✅ Acesse `https://seu-app.azurewebsites.net`
4. ✅ Tire um print e compartilhe!

### Exercício 2: Variáveis de Ambiente
1. ✅ Adicione variável `NOME_ALUNO` com seu nome
2. ✅ Modifique o código para usar: `process.env.NOME_ALUNO`
3. ✅ Faça deploy novamente
4. ✅ Veja seu nome aparecer na página!

### Exercício 3: Múltiplas Rotas
1. ✅ Adicione rota `/api/hora` que retorna a hora atual
2. ✅ Adicione rota `/sobre` com informações sobre você
3. ✅ Faça deploy e teste

### Exercício 4: Logs
1. ✅ Adicione `console.log()` em várias partes do código
2. ✅ Acesse o app algumas vezes
3. ✅ Veja os logs no "Log stream"

### Exercício 5: Desafio - Deploy de Projeto Real
1. ✅ Pegue um projeto seu do GitHub
2. ✅ Faça deploy no App Service
3. ✅ Configure variáveis de ambiente necessárias
4. ✅ Teste e compartilhe a URL!

---

## 🆘 Problemas Comuns

### App não inicia
**Erro:** "Application Error"

→ **Soluções:**
1. Veja os logs (Log stream)
2. Verifique se o `package.json` tem `"start": "node server.js"`
3. Verifique se a porta usa `process.env.PORT`
4. Garanta que `engines.node` está especificado

---

### Deploy falha
→ **Soluções:**
1. Verifique credenciais do Git
2. Certifique-se que está na branch `main` ou `master`
3. Veja "Deployment Center" → "Logs"

---

### Código antigo ainda aparece
→ **Soluções:**
1. Reinicie o App Service
2. Limpe cache do navegador (Ctrl+Shift+R)
3. Force redeploy: delete `node_modules` antes de fazer zip

---

## 🛠️ Comandos Úteis da CLI

```bash
# Listar App Services
az webapp list --output table

# Ver URL do app
az webapp show \
  --resource-group rg-aluno-SEUNOME \
  --name app-aluno-SEUNOME \
  --query defaultHostName \
  --output tsv

# Reiniciar app
az webapp restart \
  --resource-group rg-aluno-SEUNOME \
  --name app-aluno-SEUNOME

# Parar app (para economizar)
az webapp stop \
  --resource-group rg-aluno-SEUNOME \
  --name app-aluno-SEUNOME

# Iniciar app
az webapp start \
  --resource-group rg-aluno-SEUNOME \
  --name app-aluno-SEUNOME

# Deletar app (mantém o Plan)
az webapp delete \
  --resource-group rg-aluno-SEUNOME \
  --name app-aluno-SEUNOME

# Deletar App Service Plan
az appservice plan delete \
  --name plan-aluno-SEUNOME \
  --resource-group rg-aluno-SEUNOME
```

---

## 💰 Gerenciamento de Custos

### F1 (Free Tier)
- ✅ **Grátis**
- ⚠️ Limites: 60min CPU/dia, 1GB disco, 1GB RAM
- ⚠️ Dorme após 20min sem uso (cold start na próxima requisição)

### B1 (Basic)
- 💵 ~R$ 50/mês
- ✅ Sem limites de CPU/dia
- ✅ Não dorme
- ✅ SSL customizado
- ✅ 10 GB disco

**Dica:** Use F1 para aprender e testar; B1 para produção pequena.

---

## 🔗 Próximos Passos

1. **Adicionar Banco de Dados**
   - Conectar ao Azure SQL ou Cosmos DB
   - Ou usar PostgreSQL

2. **CI/CD Automático**
   - GitHub Actions para deploy automático
   - Cada push = novo deploy

3. **Application Insights**
   - Monitoramento avançado
   - Performance tracking

4. **Deployment Slots**
   - Staging environment
   - Blue-Green deployment

---

## 📖 Recursos Adicionais

- [Documentação Oficial](https://docs.microsoft.com/azure/app-service/)
- [Exemplos de Código](https://github.com/Azure-Samples/app-service-web-nodejs-get-started)
- [Preços](https://azure.microsoft.com/pricing/details/app-service/)

---

**Dúvidas?** Pergunte ao seu instrutor! 🙋

**Feito com 💙 pela equipe [ToolBox Technology](https://tbxtech.com.br/)**
