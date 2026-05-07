# 📋 Azure Policy - Explicação Detalhada

Documentação do arquivo `policy.json` - explica cada regra de bloqueio.

## 📖 Estrutura da Policy

A policy usa o efeito **"deny"** (bloquear) quando **QUALQUER** das condições abaixo for verdadeira.

---

## 🚫 Regras de Bloqueio

### 1️⃣ Bloqueia Regiões Não-Brasileiras

**O que bloqueia:**
- Qualquer recurso criado fora de Brazil South, Brazil Southeast ou Global

**Regiões permitidas:**
- `brazilsouth` - São Paulo
- `brazilsoutheast` - Rio de Janeiro  
- `global` - Para recursos globais (ex: CDN)

**Exemplo bloqueado:**
```
❌ Storage Account em "eastus" (Estados Unidos)
❌ VM em "westeurope" (Europa)
```

**Exemplo permitido:**
```
✅ Storage Account em "brazilsouth"
✅ VM em "brazilsoutheast"
```

---

### 2️⃣ Bloqueia Tipos de Recursos Não-Autorizados

**Tipos permitidos:**

| Tipo de Recurso | Para que serve |
|-----------------|----------------|
| `Microsoft.Storage/storageAccounts` | Armazenamento de arquivos |
| `Microsoft.Web/sites` | App Service (aplicações web) |
| `Microsoft.Web/sites/config` | Configurações do App Service |
| `Microsoft.Web/sites/sourcecontrols` | Deploy Git do App Service |
| `Microsoft.Web/serverfarms` | App Service Plan |
| `Microsoft.Compute/virtualMachines` | Máquinas virtuais |
| `Microsoft.Compute/disks` | Discos das VMs |
| `Microsoft.Network/networkInterfaces` | Placas de rede |
| `Microsoft.Network/virtualNetworks` | Redes virtuais |
| `Microsoft.Network/virtualNetworks/subnets` | Sub-redes |
| `Microsoft.Network/networkSecurityGroups` | Firewalls |
| `Microsoft.Network/publicIPAddresses` | IPs públicos |
| `Microsoft.KeyVault/vaults` | Cofre de segredos |
| `Microsoft.KeyVault/vaults/secrets` | Secrets no Key Vault |
| `Microsoft.Insights/components` | Application Insights |
| `Microsoft.OperationalInsights/workspaces` | Log Analytics |

**Recursos bloqueados (exemplos):**
```
❌ AKS (Kubernetes) - Microsoft.ContainerService/managedClusters
❌ Azure Functions - Microsoft.Web/sites/functions
❌ Cosmos DB - Microsoft.DocumentDB/databaseAccounts
❌ Azure SQL - Microsoft.Sql/servers
❌ Container Instances - Microsoft.ContainerInstance/containerGroups
```

---

### 3️⃣ Bloqueia VMs Grandes

**VMs permitidas (apenas série B - Burstable):**

| SKU | vCPUs | RAM | Custo/mês* |
|-----|-------|-----|------------|
| `Standard_B1s` | 1 | 1 GB | ~R$ 30 |
| `Standard_B1ms` | 1 | 2 GB | ~R$ 50 |
| `Standard_B2s` | 2 | 4 GB | ~R$ 100 |

*Valores aproximados para Brazil South, 24/7

**VMs bloqueadas (exemplos):**
```
❌ Standard_D2s_v3 (2 vCPUs, 8 GB) - ~R$ 350/mês
❌ Standard_D4s_v3 (4 vCPUs, 16 GB) - ~R$ 700/mês
❌ Standard_E4s_v3 (4 vCPUs, 32 GB) - ~R$ 800/mês
❌ Standard_F8s_v2 (8 vCPUs, 16 GB) - ~R$ 600/mês
```

💰 **Economia:** Bloqueando VMs grandes economiza até R$ 700/mês por aluno!

---

### 4️⃣ Bloqueia App Service Plans Caros

**Plans permitidos:**

| SKU | Recursos | Custo/mês |
|-----|----------|-----------|
| `F1` (Free) | 1 GB RAM, 60min CPU/dia | **Grátis** |
| `B1` (Basic) | 1.75 GB RAM, SSL customizado | ~R$ 50 |

**Plans bloqueados (exemplos):**
```
❌ S1 (Standard) - ~R$ 250/mês
❌ P1 (Premium) - ~R$ 500/mês
❌ P2 (Premium) - ~R$ 1.000/mês
```

💰 **Economia:** Até R$ 950/mês por aluno!

---

### 5️⃣ Bloqueia Storage Accounts Premium

**SKUs permitidos:**

| SKU | Tipo | Custo/GB/mês* |
|-----|------|---------------|
| `Standard_LRS` | Locally Redundant (1 datacenter) | ~R$ 0,10 |
| `Standard_GRS` | Geo Redundant (2 datacenters) | ~R$ 0,20 |

*Valores aproximados

**SKUs bloqueados:**
```
❌ Premium_LRS - ~R$ 0,70/GB (7x mais caro!)
❌ Premium_ZRS - ~R$ 0,85/GB
❌ Standard_RAGRS - ~R$ 0,40/GB (read-access geo)
```

💰 **Economia:** Até 7x mais barato com Standard!

---

### 6️⃣ Bloqueia Key Vault Premium

**SKU permitido:**

| SKU | Recursos | Custo |
|-----|----------|-------|
| `standard` | Secrets, Keys, Certificates | ~R$ 0,03/10k ops |

**SKU bloqueado:**
```
❌ premium - ~10x mais caro, HSM-backed keys
```

💰 **Para aprendizado:** Standard é suficiente!

---

## 📊 Resumo: O Que Alunos PODEM Criar

### ✅ Recursos Permitidos

**Computação:**
- ✅ VM Ubuntu/Windows (B1s, B1ms, B2s)
- ✅ App Service (F1 Free, B1 Basic)

**Armazenamento:**
- ✅ Storage Account (LRS, GRS)

**Segurança:**
- ✅ Key Vault (Standard)

**Monitoramento:**
- ✅ Application Insights
- ✅ Log Analytics Workspace

**Rede:**
- ✅ Virtual Networks, Subnets
- ✅ Network Security Groups (firewalls)
- ✅ Public IPs
- ✅ Network Interfaces

**Localização:**
- ✅ Brazil South (São Paulo)
- ✅ Brazil Southeast (Rio de Janeiro)

---

## 💰 Estimativa de Custos

### Por Aluno (Máximo Possível)

**Cenário worst-case (tudo ligado 24/7 por 30 dias):**

| Recurso | Custo/mês |
|---------|-----------|
| VM B1s (24/7) | R$ 30 |
| Storage 10GB | R$ 5 |
| App Service F1 | Grátis |
| Key Vault | R$ 5 |
| **TOTAL** | **~R$ 40** |

**30 alunos = máximo R$ 1.200/mês**

---

### Com Boas Práticas

**VMs desligadas à noite e fins de semana:**

| Recurso | Custo/mês |
|---------|-----------|
| VM B1s (8h/dia útil) | R$ 8 |
| Storage 10GB | R$ 5 |
| App Service F1 | Grátis |
| Key Vault | R$ 5 |
| **TOTAL** | **~R$ 18** |

**30 alunos = R$ 540/mês** ✅

---

### SEM a Policy (PERIGO!)

**Se um aluno criar acidentalmente:**
- VM Standard_D8s_v3: **R$ 1.400/mês**
- App Service P2: **R$ 1.000/mês**
- Storage Premium 1TB: **R$ 700/mês**

**TOTAL: R$ 3.100/mês por aluno**

**30 alunos = R$ 93.000/mês** ❌💸

---

## 🎯 Economia com a Policy

**Sem Policy:** R$ 93.000/mês (risco)
**Com Policy:** R$ 1.200/mês (máximo garantido)

**Economia: R$ 91.800/mês** 🎉

Ou **R$ 1.100.400 por ano** de economia!

---

## 🔧 Modificar a Policy

### Adicionar Nova Região

**Exemplo: Permitir East US 2**

No `policy.json`, encontre:
```json
"field": "location",
"notIn": [
  "brazilsouth",
  "brazilsoutheast",
  "global"
]
```

Adicione:
```json
"field": "location",
"notIn": [
  "brazilsouth",
  "brazilsoutheast",
  "eastus2",
  "global"
]
```

---

### Adicionar Novo Tamanho de VM

**Exemplo: Permitir B4ms (4 vCPUs, 16 GB)**

No `policy.json`, encontre:
```json
"field": "Microsoft.Compute/virtualMachines/sku.name",
"notIn": [
  "Standard_B1s",
  "Standard_B1ms",
  "Standard_B2s"
]
```

Adicione:
```json
"field": "Microsoft.Compute/virtualMachines/sku.name",
"notIn": [
  "Standard_B1s",
  "Standard_B1ms",
  "Standard_B2s",
  "Standard_B4ms"
]
```

⚠️ **Atenção:** B4ms custa ~R$ 200/mês!

---

### Permitir Novo Tipo de Recurso

**Exemplo: Permitir Azure Functions**

No `policy.json`, na lista de tipos permitidos, adicione:
```json
"Microsoft.Web/sites/functions"
```

---

## 📖 Recursos Adicionais

- [Azure Policy Docs](https://docs.microsoft.com/azure/governance/policy/)
- [VM Pricing](https://azure.microsoft.com/pricing/details/virtual-machines/)
- [App Service Pricing](https://azure.microsoft.com/pricing/details/app-service/)
- [Storage Pricing](https://azure.microsoft.com/pricing/details/storage/)

---

**Feito com 💙 pela equipe [ToolBox Technology](https://tbxtech.com.br/)**
