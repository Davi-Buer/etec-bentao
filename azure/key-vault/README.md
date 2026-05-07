# 🔐 Azure Key Vault - Exercício Prático

Guarde senhas e segredos de forma segura na nuvem!

## 📚 O que você vai aprender

- Criar um Azure Key Vault
- Armazenar secrets (senhas, chaves de API)
- Usar secrets em aplicações
- Controlar acessos e permissões
- Boas práticas de segurança

---

## 🎯 O que é Key Vault?

**Definição:**
É um serviço para armazenar e gerenciar **secrets**, **chaves criptográficas** e **certificados** de forma segura.

**Problemas que resolve:**

❌ **Antes (ERRADO):**
```javascript
// ⚠️ NUNCA FAÇA ISSO!
const senha = "minhaSenha123";
const apiKey = "abc123xyz789";
```

✅ **Com Key Vault (CORRETO):**
```javascript
// Senha vem do Key Vault, não está no código!
const senha = await getSecretFromKeyVault("DbPassword");
```

---

## 🔑 Tipos de Segredos

### 1. Secrets (Segredos)
**O que guardar:**
- Senhas de banco de dados
- Chaves de API (OpenAI, Stripe, etc)
- Connection strings
- Tokens de acesso

### 2. Keys (Chaves criptográficas)
**O que guardar:**
- Chaves de criptografia RSA
- Chaves de assinatura digital

### 3. Certificates (Certificados)
**O que guardar:**
- Certificados SSL/TLS
- Certificados de autenticação

💡 **Para este curso:** Vamos focar em **Secrets** (é o mais usado).

---

## 🚀 Parte 1: Criar Key Vault no Portal

### Passo 1: Criar o Key Vault

**1. Acesse o Portal Azure:**
```
https://portal.azure.com
```

**2. Pesquise por "Key vaults"**

**3. Clique em "+ Create"**

---

### Passo 2: Configurações Básicas

#### **Aba: Basics**

| Campo | Valor | Explicação |
|-------|-------|------------|
| **Subscription** | Sua assinatura | Fornecida pelo instrutor |
| **Resource group** | `rg-aluno-SEUNOME` | Use existente ou crie novo |
| **Key vault name** | `kv-aluno-SEUNOME` | Ex: `kv-aluno-joao` (único globalmente!) |
| **Region** | `Brazil South` | Onde os dados ficam armazenados |
| **Pricing tier** | `Standard` | Suficiente para aprendizado |

⚠️ **Nome precisa ser único globalmente!** Se `kv-aluno-joao` já existe, use `kv-aluno-joao-123`

---

#### **Aba: Access configuration**

| Campo | Valor |
|-------|-------|
| **Permission model** | `Vault access policy` |
| **Enable access to:** | Marque "Azure Virtual Machines for deployment" (opcional) |

💡 Deixe o resto no padrão.

**4. Clique em "Review + create"**

**5. Clique em "Create"**

**6. Aguarde 1-2 minutos**

---

## 🔒 Parte 2: Adicionar Secrets

### Adicionar um Secret via Portal

**1. Vá até o Key Vault criado**

**2. No menu lateral, clique em "Secrets"**

**3. Clique em "+ Generate/Import"**

**4. Preencha:**

| Campo | Valor de Exemplo |
|-------|------------------|
| **Upload options** | Manual |
| **Name** | `DatabasePassword` |
| **Value** | `MinhaS3nh@Segura!` |
| **Content type** | `password` (opcional) |
| **Set activation date** | (deixe vazio) |
| **Set expiration date** | (deixe vazio) |
| **Enabled** | Yes ✅ |

**5. Clique em "Create"**

✅ **Pronto!** Sua senha está segura no Key Vault!

---

### Adicionar múltiplos secrets

**Exemplos de secrets úteis:**

| Secret Name | Secret Value | Quando usar |
|-------------|--------------|-------------|
| `DatabasePassword` | `S3nh@Segura!` | Senha do banco de dados |
| `OpenAI-ApiKey` | `sk-abc123...` | Chave da API OpenAI |
| `StorageConnectionString` | `DefaultEndpoints...` | Connection string do Storage |
| `JwtSecretKey` | `meuTokenSecreto123` | Chave para assinar JWTs |
| `SmtpPassword` | `senha-email` | Senha de servidor de email |

---

## 🔑 Parte 3: Gerenciar Acesso

### Dar Permissão para Você

**1. No Key Vault, vá em "Access policies"**

**2. Clique em "+ Create"**

**3. Selecione permissões:**

**Secret permissions:**
- ✅ Get (ler secrets)
- ✅ List (listar secrets)
- ✅ Set (criar/atualizar secrets)
- ✅ Delete (deletar secrets) - cuidado!

**4. Clique em "Next"**

**5. Em "Principal", selecione seu usuário**

**6. Clique em "Next" → "Next" → "Create"**

---

### Dar Permissão para uma Aplicação

**Cenário:** App Service precisa ler secrets

**1. Habilite Managed Identity no App Service:**
```bash
az webapp identity assign \
  --resource-group rg-aluno-SEUNOME \
  --name app-aluno-SEUNOME
```

**2. Copie o Object ID retornado**

**3. No Key Vault:**
- "Access policies" → "+ Create"
- Selecione permissões: **Get**, **List**
- Em Principal, cole o Object ID
- Create

---

## 💻 Parte 4: Usar Secrets na Aplicação

### Via Azure CLI (Simples)

```bash
# Ler um secret
az keyvault secret show \
  --vault-name kv-aluno-SEUNOME \
  --name DatabasePassword \
  --query value \
  --output tsv
```

---

### Via Node.js

**1. Instalar biblioteca:**
```bash
npm install @azure/keyvault-secrets @azure/identity
```

**2. Código:**

```javascript
const { SecretClient } = require("@azure/keyvault-secrets");
const { DefaultAzureCredential } = require("@azure/identity");

// URL do seu Key Vault
const vaultUrl = "https://kv-aluno-SEUNOME.vault.azure.net";

// Cliente para acessar secrets
const credential = new DefaultAzureCredential();
const client = new SecretClient(vaultUrl, credential);

async function getSecret(secretName) {
  try {
    const secret = await client.getSecret(secretName);
    return secret.value;
  } catch (error) {
    console.error(`Erro ao buscar secret: ${error.message}`);
    throw error;
  }
}

// Usar na aplicação
async function main() {
  const dbPassword = await getSecret("DatabasePassword");
  const apiKey = await getSecret("OpenAI-ApiKey");
  
  console.log("Senha do DB:", dbPassword);
  console.log("API Key:", apiKey);
  
  // Usar para conectar ao banco, etc
}

main();
```

---

### Via Python

**1. Instalar biblioteca:**
```bash
pip install azure-keyvault-secrets azure-identity
```

**2. Código:**

```python
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

# URL do Key Vault
vault_url = "https://kv-aluno-SEUNOME.vault.azure.net"

# Cliente
credential = DefaultAzureCredential()
client = SecretClient(vault_url=vault_url, credential=credential)

def get_secret(secret_name):
    try:
        secret = client.get_secret(secret_name)
        return secret.value
    except Exception as e:
        print(f"Erro ao buscar secret: {e}")
        raise

# Usar
db_password = get_secret("DatabasePassword")
api_key = get_secret("OpenAI-ApiKey")

print(f"Senha: {db_password}")
print(f"API Key: {api_key}")
```

---

## 🔐 Parte 5: Boas Práticas de Segurança

### ✅ O que FAZER

1. **Use Managed Identity sempre que possível**
   - App Service, VM, Functions podem acessar sem senha!

2. **Princípio do menor privilégio**
   - Dê apenas as permissões necessárias
   - App só lê? Dê apenas "Get", não "Delete"

3. **Rotacione secrets regularmente**
   - Mude senhas a cada 90 dias
   - Use "Set expiration date"

4. **Use nomes descritivos**
   - ✅ `DatabasePassword-Production`
   - ❌ `senha1`

5. **Habilite logs e auditoria**
   - Veja quem acessou o quê e quando

---

### ❌ O que NÃO FAZER

1. **❌ NUNCA commite secrets no Git**
   ```javascript
   // ❌ ERRADO!
   const senha = "abc123";
   
   // ✅ CORRETO!
   const senha = await getSecretFromKeyVault("DbPassword");
   ```

2. **❌ Não imprima secrets em logs**
   ```javascript
   // ❌ ERRADO!
   console.log(`Senha: ${password}`);
   
   // ✅ CORRETO!
   console.log("Senha carregada com sucesso");
   ```

3. **❌ Não envie secrets por email/chat**
   - Use Key Vault e dê acesso à pessoa

4. **❌ Não dê permissões amplas desnecessárias**
   - ❌ Dar permissão "All" para todo mundo
   - ✅ Dar apenas "Get" para quem precisa ler

---

## 📝 Exercícios Práticos

### Exercício 1: Primeiro Secret
1. ✅ Crie um Key Vault
2. ✅ Adicione um secret chamado `MinhaSenha` com valor `S3nh@Teste!`
3. ✅ Leia o secret via portal
4. ✅ Tire um print mostrando o secret (pode mostrar só o nome)

### Exercício 2: Via CLI
1. ✅ Instale Azure CLI (se ainda não tem)
2. ✅ Faça login: `az login`
3. ✅ Leia o secret via CLI:
   ```bash
   az keyvault secret show \
     --vault-name kv-aluno-SEUNOME \
     --name MinhaSenha
   ```

### Exercício 3: Múltiplos Secrets
1. ✅ Adicione 3 secrets diferentes:
   - `ApiKey-Development` → `dev-key-123`
   - `ApiKey-Production` → `prod-key-456`
   - `EmailPassword` → `senha-email-789`
2. ✅ Liste todos os secrets via CLI:
   ```bash
   az keyvault secret list --vault-name kv-aluno-SEUNOME
   ```

### Exercício 4: Usar em Código
1. ✅ Crie um script Node.js ou Python
2. ✅ Leia um secret do Key Vault
3. ✅ Imprima apenas "Secret carregado com sucesso!" (não imprima o valor!)

### Exercício 5: Desafio - Integração
1. ✅ Se você tem um App Service:
   - Habilite Managed Identity
   - Dê permissão ao Key Vault
   - Modifique o código para ler secrets do Key Vault
   - Teste a aplicação

---

## 🛠️ Comandos Úteis da CLI

```bash
# Criar Key Vault
az keyvault create \
  --name kv-aluno-SEUNOME \
  --resource-group rg-aluno-SEUNOME \
  --location brazilsouth

# Adicionar secret
az keyvault secret set \
  --vault-name kv-aluno-SEUNOME \
  --name "DatabasePassword" \
  --value "MinhaS3nh@Segura"

# Ler secret
az keyvault secret show \
  --vault-name kv-aluno-SEUNOME \
  --name "DatabasePassword" \
  --query value \
  --output tsv

# Listar todos os secrets
az keyvault secret list \
  --vault-name kv-aluno-SEUNOME \
  --output table

# Deletar secret
az keyvault secret delete \
  --vault-name kv-aluno-SEUNOME \
  --name "DatabasePassword"

# Dar permissão a um usuário
az keyvault set-policy \
  --name kv-aluno-SEUNOME \
  --upn usuario@dominio.com \
  --secret-permissions get list set

# Dar permissão a Managed Identity
az keyvault set-policy \
  --name kv-aluno-SEUNOME \
  --object-id <OBJECT-ID-DA-IDENTIDADE> \
  --secret-permissions get list
```

---

## 🆘 Problemas Comuns

### Não consigo criar Key Vault
**Erro:** "Name already exists"

→ Nome do Key Vault precisa ser único globalmente! Use um sufixo:
- ✅ `kv-aluno-joao-123`
- ✅ `kv-aluno-joao-2024`

---

### Não consigo acessar secrets
**Erro:** "Forbidden" ou "Access denied"

→ **Soluções:**
1. Verifique se você tem permissão (Access policies)
2. Se usando Managed Identity, verifique se está habilitada
3. Verifique se o Object ID está correto

---

### Código não funciona localmente
**Erro:** "DefaultAzureCredential failed"

→ **Soluções:**
1. Faça login no Azure CLI: `az login`
2. Ou use variáveis de ambiente com Service Principal
3. Localmente, pode usar a extensão do VS Code

---

## 💰 Custos

**Preços (aproximados):**
- **Key Vault Standard:** ~R$ 0,03 por 10.000 operações
- **Armazenamento de secrets:** Primeiros 10.000 grátis!
- **Custo mensal típico:** < R$ 5/mês

💡 **É muito barato!** O custo de segurança vale muito a pena.

---

## 🔗 Casos de Uso Reais

### 1. Aplicação Web com Banco de Dados
```
App Service → Key Vault (senha do DB) → Azure SQL Database
```

### 2. API com Chaves de Terceiros
```
API → Key Vault (OpenAI API Key, Stripe Key) → Serviços externos
```

### 3. Deploy Automático (CI/CD)
```
GitHub Actions → Key Vault (credenciais) → Deploy na produção
```

---

## 📖 Próximos Passos

1. **Integrar com Application Insights**
   - Monitor quem acessa secrets

2. **Usar com Azure Functions**
   - Functions lendo secrets

3. **Rotação Automática**
   - Mudar senhas automaticamente

4. **Backup e Recovery**
   - Fazer backup dos secrets

---

## 📚 Recursos Adicionais

- [Documentação Oficial](https://docs.microsoft.com/azure/key-vault/)
- [Melhores Práticas](https://docs.microsoft.com/azure/key-vault/general/best-practices)
- [Exemplos de Código](https://github.com/Azure-Samples/key-vault-node-quickstart)

---

**🔐 Resumo: Key Vault = Cofre para senhas na nuvem!**

**Dúvidas?** Pergunte ao seu instrutor! 🙋

**Feito com 💙 pela equipe [ToolBox Technology](https://tbxtech.com.br/)**
