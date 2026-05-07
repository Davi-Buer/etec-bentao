# 📋 Azure Policy - Governança e Controle de Custos

Configure regras para controlar quais recursos podem ser criados e seus tamanhos!

## 📚 O que você vai aprender

- O que é Azure Policy
- Por que usar policies
- Aplicar policy de controle de custos
- Bloquear recursos caros
- Forçar uso de regiões específicas

---

## 🎯 O que é Azure Policy?

**Definição:**
É um serviço para criar e aplicar **regras** que controlam os recursos do Azure.

**Exemplos de regras:**
- ✅ Permitir apenas VMs pequenas (B1s)
- ✅ Bloquear criação de recursos muito caros
- ✅ Forçar uso da região Brazil South
- ✅ Exigir tags em todos os recursos
- ✅ Bloquear Storage Account Premium

---

## 💡 Por Que Usar Policies?

### Problema Comum

**Sem Policy:**
```
Aluno cria VM de R$ 2.000/mês por engano
       ↓
Conta do Azure explode! 💸
```

**Com Policy:**
```
Aluno tenta criar VM cara
       ↓
Azure bloqueia: "Apenas VMs B1s, B1ms, B2s permitidas" ✋
       ↓
Custo controlado! ✅
```

---

### Casos de Uso

| Problema | Solução com Policy |
|----------|-------------------|
| 💸 Custos altos | Bloquear recursos caros |
| 🌍 Conformidade LGPD | Forçar recursos no Brasil |
| 🏷️ Desorganização | Exigir tags em recursos |
| 🔒 Segurança | Bloquear IPs públicos em VMs |
| 📊 Auditoria | Registrar todos os recursos criados |

---

## 🚀 Parte 1: Entender a Policy do Curso

Este repositório já vem com uma policy de controle de custos!

### Arquivo: `policy.json`

**O que essa policy faz:**

#### ✅ Permite Apenas Estes Recursos:
- Storage Accounts (armazenamento)
- Virtual Machines (VMs)
- App Services (PaaS)
- Key Vaults (segredos)
- Application Insights (monitoramento)
- Log Analytics Workspace (logs)
- Recursos de rede (VNet, IP, NSG)

#### ✅ Permite Apenas Estes Tamanhos:

**VMs:**
- Standard_B1s (1 vCPU, 1 GB RAM) ~R$ 30/mês
- Standard_B1ms (1 vCPU, 2 GB RAM) ~R$ 50/mês
- Standard_B2s (2 vCPU, 4 GB RAM) ~R$ 100/mês

**App Service Plans:**
- F1 (Free tier) - Grátis!
- B1 (Basic) ~R$ 50/mês

**Storage Accounts:**
- Standard_LRS (Locally Redundant)
- Standard_GRS (Geo Redundant)

**Key Vaults:**
- Standard (não Premium)

#### ✅ Permite Apenas Estas Regiões:
- Brazil South (São Paulo)
- Brazil Southeast (Rio de Janeiro) 
- Global (para recursos globais)

#### ❌ Bloqueia Tudo Que Não Está na Lista!

---

## 🛠️ Parte 2: Aplicar a Policy

### Via Portal Azure

**1. Acesse o Portal:**
```
https://portal.azure.com
```

**2. Pesquise por "Policy"**

**3. No menu lateral, clique em "Definitions"**

**4. Clique em "+ Policy definition"**

**5. Preencha:**

| Campo | Valor |
|-------|-------|
| **Definition location** | Sua assinatura |
| **Name** | `Policy-Controle-Custos-Alunos` |
| **Description** | `Bloqueia recursos caros para controlar custos` |
| **Category** | Crie nova: `Educação` |

**6. Em "Policy rule":**
- Copie todo o conteúdo de `policy.json`
- Cole no editor

**7. Clique em "Save"**

---

### Atribuir a Policy

**Agora que criamos a policy, precisamos aplicá-la!**

**1. Vá em "Assignments" (no menu Policy)**

**2. Clique em "+ Assign policy"**

**3. Preencha:**

| Campo | Valor |
|-------|-------|
| **Scope** | Selecione o Resource Group dos alunos |
| **Policy definition** | Procure `Policy-Controle-Custos-Alunos` |
| **Assignment name** | `Aplicar Controle de Custos` |
| **Enforcement** | **Enabled** ✅ (bloqueia de verdade!) |

**4. Clique em "Review + create"**

**5. Clique em "Create"**

✅ **Pronto! Policy ativa!**

---

### Via Azure CLI

```bash
# 1. Criar a policy definition
az policy definition create \
  --name 'Policy-Controle-Custos-Alunos' \
  --display-name 'Controle de Custos para Alunos' \
  --description 'Bloqueia recursos caros' \
  --rules @policy.json \
  --mode All

# 2. Atribuir ao Resource Group
az policy assignment create \
  --name 'aplicar-controle-custos' \
  --display-name 'Aplicar Controle de Custos' \
  --policy 'Policy-Controle-Custos-Alunos' \
  --scope "/subscriptions/SEU-SUBSCRIPTION-ID/resourceGroups/rg-aluno-SEUNOME"
```

---

## 🧪 Parte 3: Testar a Policy

### Teste 1: Tentar Criar VM Grande (Deve Bloquear) ❌

**1. Tente criar uma VM Standard_D2s_v3 (cara!)**

**2. Resultado esperado:**
```
❌ Resource creation was disallowed by policy.

Policy: Policy-Controle-Custos-Alunos
Reason: VM size 'Standard_D2s_v3' is not allowed.
Allowed sizes: Standard_B1s, Standard_B1ms, Standard_B2s
```

✅ **Policy funcionando!** Bloqueou a VM cara!

---

### Teste 2: Criar VM Pequena (Deve Permitir) ✅

**1. Crie uma VM Standard_B1s**

**2. Resultado esperado:**
```
✅ Deployment succeeded
```

✅ **Policy permitiu!** B1s está na lista de permitidos.

---

### Teste 3: Tentar Criar Kubernetes (Deve Bloquear) ❌

**1. Tente criar um Azure Kubernetes Service (AKS)**

**2. Resultado esperado:**
```
❌ Resource creation was disallowed by policy.

Policy: Policy-Controle-Custos-Alunos
Reason: Resource type 'Microsoft.ContainerService/managedClusters' is not allowed.
```

✅ **Policy bloqueou!** AKS não está na lista.

---

## 📋 Parte 4: Entender a Estrutura da Policy

### Anatomia do `policy.json`

```json
{
  "mode": "All",              // Aplica a todos os recursos
  "policyRule": {
    "if": {                   // SE a condição for verdadeira...
      "anyOf": [              // ...qualquer uma dessas condições
        {
          // Condição 1: Região não permitida
          "field": "location",
          "notIn": ["brazilsouth", "brazilsoutheast", "global"]
        },
        {
          // Condição 2: Tipo de recurso não permitido
          "field": "type",
          "notIn": ["Microsoft.Storage/storageAccounts", ...]
        },
        {
          // Condição 3: VM de tamanho não permitido
          "field": "Microsoft.Compute/virtualMachines/sku.name",
          "notIn": ["Standard_B1s", "Standard_B1ms", "Standard_B2s"]
        }
      ]
    },
    "then": {
      "effect": "deny"        // ...ENTÃO bloqueia (nega)
    }
  }
}
```

---

### Efeitos Possíveis

| Efeito | O que faz | Quando usar |
|--------|-----------|-------------|
| **Deny** | Bloqueia criação | Controle de custos (use este!) |
| **Audit** | Permite mas registra | Monitoramento sem bloqueio |
| **Append** | Adiciona tags automaticamente | Organização |
| **DeployIfNotExists** | Cria recurso adicional se não existir | Compliance |
| **Modify** | Modifica propriedades | Correção automática |

💡 **Para este curso:** Usamos **Deny** (bloqueia de verdade!)

---

## 📝 Exercícios Práticos

### Exercício 1: Aplicar a Policy
1. ✅ No Portal, crie a policy definition com o conteúdo de `policy.json`
2. ✅ Atribua ao Resource Group dos alunos
3. ✅ Aguarde 5 minutos para policy propagar

### Exercício 2: Testar Bloqueio de VM
1. ✅ Tente criar uma VM **Standard_D2s_v3**
2. ✅ Veja a mensagem de erro
3. ✅ Tire um print mostrando o bloqueio
4. ✅ Crie uma VM **Standard_B1s** (deve funcionar)

### Exercício 3: Testar Bloqueio de Região
1. ✅ Tente criar um Storage Account na região **East US**
2. ✅ Deve ser bloqueado!
3. ✅ Crie na região **Brazil South** (deve funcionar)

### Exercício 4: Ver Compliance
1. ✅ Vá em "Policy" → "Compliance"
2. ✅ Veja quais recursos estão em conformidade
3. ✅ Se houver recursos não-conformes, veja o que são

---

## 🛠️ Customizar a Policy

### Adicionar Nova Região Permitida

**Cenário:** Permitir também **East US 2**

**No `policy.json`, encontre:**
```json
"field": "location",
"notIn": [
  "brazilsouth",
  "brazilsoutheast",
  "global"
]
```

**Adicione East US 2:**
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

**Cenário:** Permitir também **B2ms** (2 vCPU, 8 GB RAM)

**No `policy.json`, encontre:**
```json
"field": "Microsoft.Compute/virtualMachines/sku.name",
"notIn": [
  "Standard_B1s",
  "Standard_B1ms",
  "Standard_B2s"
]
```

**Adicione B2ms:**
```json
"field": "Microsoft.Compute/virtualMachines/sku.name",
"notIn": [
  "Standard_B1s",
  "Standard_B1ms",
  "Standard_B2s",
  "Standard_B2ms"
]
```

---

### Permitir Novo Tipo de Recurso

**Cenário:** Permitir **Azure Functions**

**No `policy.json`, encontre a seção de tipos permitidos:**
```json
"field": "type",
"notIn": [
  "Microsoft.Storage/storageAccounts",
  "Microsoft.Web/sites",
  ...
]
```

**Adicione Functions:**
```json
"field": "type",
"notIn": [
  "Microsoft.Storage/storageAccounts",
  "Microsoft.Web/sites",
  "Microsoft.Web/sites/functions",    // ← NOVO!
  ...
]
```

---

## 🆘 Problemas Comuns

### Policy não está bloqueando
→ **Soluções:**
1. Aguarde 5-10 minutos para propagar
2. Verifique se está "Enabled" (não "Disabled")
3. Veja se o scope está correto (Resource Group certo?)
4. Force refresh: delete e recrie a assignment

### Recurso bloqueado incorretamente
→ **Soluções:**
1. Verifique a sintaxe JSON da policy
2. Teste em modo "Audit" primeiro (não bloqueia)
3. Veja os logs de compliance

### Como remover a policy temporariamente
→ **No Portal:**
1. Vá em "Policy" → "Assignments"
2. Selecione a policy
3. Clique em "Delete assignment"

---

## 💰 Estimativa de Custos COM Policy

**Sem Policy (perigo!):**
- Aluno cria VM Standard_D4s_v3: **~R$ 400/mês**
- 30 alunos: **R$ 12.000/mês** 💸

**Com Policy (seguro!):**
- Alunos só criam VMs B1s: **~R$ 30/mês**
- 30 alunos: **R$ 900/mês** ✅

**Economia: R$ 11.100/mês!**

---

## 📊 Monitoramento de Compliance

### Ver Recursos Não-Conformes

**1. Vá em "Policy" → "Compliance"**

**2. Veja:**
- % de recursos em conformidade
- Quais recursos violam policies
- Quais policies têm mais violações

**3. Para cada recurso não-conforme:**
- Veja a policy violada
- Veja o motivo da violação
- Decida: corrigir ou adicionar exceção

---

## 🎓 Policies Úteis Adicionais

### 1. Exigir Tags

**Use case:** Todo recurso deve ter tag `Dono` e `Projeto`

```json
{
  "if": {
    "anyOf": [
      {
        "field": "tags['Dono']",
        "exists": "false"
      },
      {
        "field": "tags['Projeto']",
        "exists": "false"
      }
    ]
  },
  "then": {
    "effect": "deny"
  }
}
```

---

### 2. Bloquear IPs Públicos em VMs

**Use case:** VMs não podem ter IP público (segurança)

```json
{
  "if": {
    "allOf": [
      {
        "field": "type",
        "equals": "Microsoft.Network/networkInterfaces"
      },
      {
        "field": "Microsoft.Network/networkInterfaces/ipConfigurations[*].publicIPAddress.id",
        "exists": "true"
      }
    ]
  },
  "then": {
    "effect": "deny"
  }
}
```

---

## 📖 Recursos Adicionais

- [Documentação Oficial](https://docs.microsoft.com/azure/governance/policy/)
- [Exemplos de Policies](https://github.com/Azure/azure-policy)
- [Policy Samples](https://docs.microsoft.com/azure/governance/policy/samples/)
- [Tutorial Interativo](https://docs.microsoft.com/learn/modules/build-cloud-governance-strategy-azure/)

---

## 📊 Resumo

**Azure Policy:**
- 📋 Define regras de governança
- 💰 Controla custos
- 🔒 Garante segurança
- 📊 Monitora compliance

**Para este curso:**
- Bloqueia VMs caras
- Força uso de regiões brasileiras
- Permite apenas recursos educacionais
- **Economiza muito dinheiro!** 💰

---

**⚠️ IMPORTANTE PARA INSTRUTORES:**

Sempre aplique a policy ANTES de dar acesso aos alunos!

1. Crie as accounts dos alunos
2. Aplique a policy no Resource Group ou Subscription
3. Aguarde 10 minutos
4. Teste você mesmo
5. Libere para os alunos

---

**Dúvidas?** Pergunte ao administrador! 🙋

**Feito com 💙 pela equipe [ToolBox Technology](https://tbxtech.com.br/)**
