# Azure Storage Account - Exercício Prático

Um guia completo para criar e usar um Azure Storage Account na prática.

## 📚 O que você vai aprender

**Parte 1 - Armazenamento de Arquivos:**
- Criar um Storage Account no Azure
- Fazer upload e download de arquivos (Blobs)
- Criar e usar Containers
- Acessar seus arquivos via Python
- Gerenciar permissões básicas

**Parte 2 - Hospedagem de Sites:** 🌐
- Hospedar um site HTML estático no Azure
- Configurar Static Website Hosting
- Publicar seu próprio site na internet
- Ver o guia em: [`website/README.md`](website/README.md)

---

## 🎯 Parte 1: Criar o Storage Account no Portal

**1. Acesse o Portal do Azure**
```
https://portal.azure.com
```
Entre com a conta que seu instrutor forneceu.

**2. Criar o Storage Account**

1. No menu lateral, clique em **"Criar um recurso"**
2. Pesquise por **"Storage Account"**
3. Clique em **"Criar"**

**3. Preencha os dados básicos:**

| Campo | Valor |
|-------|-------|
| **Assinatura** | Use a assinatura da organização |
| **Grupo de Recursos** | Crie um novo: `rg-aluno-SEUNOME` (ex: `rg-aluno-joao`) |
| **Nome da Storage Account** | `stalgseunome` (ex: `stalgjoao`) ⚠️ Só letras minúsculas e números! |
| **Região** | `Brazil South` |
| **Performance** | `Standard` |
| **Redundância** | `LRS (Locally Redundant Storage)` |

4. Clique em **"Revisar + Criar"**
5. Clique em **"Criar"**
6. Aguarde 1-2 minutos até a implantação terminar

**4. Copie suas credenciais:**

Após criar, vá até o recurso e clique em **"Chaves de acesso"** (Access keys):
- Copie o **Nome da conta** (Storage account name)
- Copie a **Connection string** da Key1

⚠️ **IMPORTANTE:** Guarde essa connection string! Vamos usar nos scripts.

---

## 🗂️ Parte 2: Criar um Container (via Portal)

Containers são como "pastas" onde você guarda seus arquivos (blobs).

**1. No seu Storage Account:**
- No menu lateral, clique em **"Containers"**
- Clique em **"+ Container"**
- Nome: `documentos`
- Nível de acesso: **Privado**
- Clique em **"Criar"**

**2. Fazer upload de um arquivo manualmente:**
- Clique no container `documentos`
- Clique em **"Upload"**
- Selecione um arquivo qualquer (ex: uma foto ou PDF)
- Clique em **"Upload"**

✅ Pronto! Você já tem um arquivo na nuvem!

---

## 💻 Parte 3: Usar via Script Python

Agora vamos automatizar o upload/download com código.

**1. Instalar as dependências:**
```bash
cd azure/storage
pip install -r requirements.txt
```

**2. Configurar suas credenciais:**
```bash
cp .env.example .env
nano .env
```

Cole sua **Connection String** no arquivo `.env`:
```env
AZURE_STORAGE_CONNECTION_STRING="DefaultEndpointsProtocol=https;AccountName=..."
```

**3. Upload de arquivo:**
```bash
python upload_file.py meu-arquivo.txt
```

**4. Download de arquivo:**
```bash
python download_file.py meu-arquivo.txt
```

**5. Listar todos os arquivos:**
```bash
python list_files.py
```

---

## 📝 Exercícios Práticos

### Exercício 1: Upload de múltiplos arquivos
1. Crie 3 arquivos de texto diferentes
2. Use o script `upload_file.py` para fazer upload de cada um
3. Use `list_files.py` para confirmar que todos foram enviados

### Exercício 2: Organização com containers
1. Crie um novo container chamado `imagens` (via portal ou script)
2. Faça upload de 2 imagens diferentes
3. Liste os arquivos do container `imagens`

### Exercício 3: Download e verificação
1. Delete um arquivo localmente
2. Baixe ele novamente do Azure usando `download_file.py`
3. Confirme que o conteúdo está correto

### Exercício 4: Desafio - Backup automático
Modifique o script `upload_file.py` para:
- Fazer upload de todos os arquivos `.txt` de uma pasta
- Mostrar o tamanho de cada arquivo enviado
- Exibir uma mensagem de sucesso para cada upload

---

## 🔍 Conceitos Importantes

### O que é um Storage Account?
É um "espaço de armazenamento na nuvem" da Azure onde você pode guardar:
- **Blobs** (arquivos como PDFs, imagens, vídeos)
- **Files** (compartilhamento de arquivos como um drive de rede)
- **Tables** (dados estruturados)
- **Queues** (filas de mensagens)

### O que é um Container?
É como uma "pasta" dentro do Storage Account. Você organiza seus blobs (arquivos) dentro de containers.

### O que é uma Connection String?
É como uma "senha completa" que tem todas as informações para acessar seu Storage Account. **Nunca compartilhe publicamente!**

---

## 🛠️ Comandos Úteis

```bash
# Instalar Azure CLI (se ainda não tiver)
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Fazer login no Azure
az login

# Listar seus storage accounts
az storage account list --output table

# Criar um container via CLI
az storage container create --name "novocontainer" --connection-string "$AZURE_STORAGE_CONNECTION_STRING"

# Fazer upload via CLI
az storage blob upload \
  --container-name documentos \
  --name arquivo.txt \
  --file ./arquivo.txt \
  --connection-string "$AZURE_STORAGE_CONNECTION_STRING"
```

---

## 🧹 Limpeza (ao final do exercício)

**Via Portal:**
1. Vá até **"Grupos de recursos"**
2. Selecione `rg-aluno-SEUNOME`
3. Clique em **"Excluir grupo de recursos"**
4. Digite o nome do grupo para confirmar
5. Clique em **"Excluir"**

⚠️ Isso vai deletar TUDO (Storage Account + arquivos).

---

## 📚 Estrutura do Projeto

```
azure/storage/
├── README.md              # Este guia
├── requirements.txt       # Dependências Python
├── .env.example          # Modelo de configuração
├── upload_file.py        # Script para upload
├── download_file.py      # Script para download
├── list_files.py         # Script para listar arquivos
└── create_container.py   # Script para criar container
```

---

## 🆘 Problemas Comuns

### Erro: "The specified container does not exist"
→ Você precisa criar o container `documentos` primeiro (veja Parte 2)

### Erro: "Invalid connection string"
→ Verifique se você copiou a connection string completa no `.env`

### Erro: "Authentication failed"
→ Sua connection string pode estar expirada. Pegue uma nova no portal.

### Script não encontra o arquivo
→ Certifique-se de estar na pasta `azure/storage/` quando executar os comandos

---

## 🎓 Recursos Adicionais

- [Documentação oficial do Azure Storage](https://docs.microsoft.com/azure/storage/)
- [Azure Storage Explorer](https://azure.microsoft.com/features/storage-explorer/) - App visual para gerenciar storage
- [Tutorial interativo Microsoft Learn](https://docs.microsoft.com/learn/modules/store-app-data-with-azure-blob-storage/)

---

**Dúvidas?** Pergunte ao seu instrutor! 🙋
