# ☁️ Conceitos Básicos de Cloud - Guia Rápido

Versão resumida dos conceitos essenciais de cloud computing (30-45 minutos de leitura).

## 🎯 O que é Cloud?

**Em poucas palavras:**
Usar recursos de computação pela internet pagando apenas pelo que você usa.

**Analogia simples:**
- ❌ Antes: Comprar um gerador para ter energia
- ✅ Cloud: Usar energia da rede elétrica e pagar a conta

---

## 💡 Por que usar Cloud?

| ✅ Vantagens | Exemplo Prático |
|-------------|-----------------|
| 💰 Pague só o que usar | VM ligada 8h/dia = paga 8h, não 24h |
| 📈 Cresce ou diminui conforme necessário | Black Friday: +100 servidores; Janeiro: -100 servidores |
| ⚡ Recursos em minutos | VM pronta em 5 min vs. comprar servidor (semanas) |
| 🌍 Disponível globalmente | Seu site acessível do Brasil, EUA, Europa... |

---

## 🏗️ 3 Tipos de Cloud (IaaS, PaaS, SaaS)

### 🔧 IaaS - Infrastructure as a Service
**Você aluga a infraestrutura**

- Exemplo: Azure Virtual Machine, AWS EC2
- Use quando: Quer controle total do servidor

### 🛠️ PaaS - Platform as a Service
**Você só se preocupa com a aplicação**

- Exemplo: Heroku, Azure App Service
- Use quando: Quer focar no código, não em infraestrutura

### 📦 SaaS - Software as a Service
**Software pronto para usar**

- Exemplo: Gmail, Microsoft 365, Netflix
- Use quando: Só quer usar, não instalar/gerenciar

---

## 📊 Comparação Rápida

```
           O QUE VOCÊ GERENCIA?

           IaaS    PaaS    SaaS
           ━━━━    ━━━━    ━━━━
Aplicação   ✅      ✅      ❌
Dados       ✅      ✅      ✅
Sistema     ✅      ❌      ❌
Servidores  ❌      ❌      ❌
Rede        ❌      ❌      ❌
```

**Resumo:**
- Mais controle → IaaS
- Equilíbrio → PaaS
- Mais simples → SaaS

---

## 🌍 Principais Provedores

| Provedor | Forte em | Exemplo de Serviço |
|----------|----------|-------------------|
| ☁️ **Azure** | Windows, Office 365 | Virtual Machines, Storage |
| 🔍 **Google Cloud** | Big Data, AI/ML | Compute Engine, BigQuery |
| 📦 **AWS** | Maior variedade | EC2, S3, Lambda |

💡 **Para este curso:** Usamos principalmente Azure!

---

## 🛠️ Recursos Mais Comuns

### 1. Computação (VMs)
- **O que é:** Computador virtual na nuvem
- **Exemplo:** Azure Virtual Machine (Ubuntu)
- **Quando usar:** Rodar aplicações, hospedar sites

### 2. Armazenamento (Storage)
- **O que é:** Guardar arquivos na nuvem
- **Exemplo:** Azure Blob Storage
- **Quando usar:** Backups, imagens, vídeos, sites estáticos

### 3. Banco de Dados
- **O que é:** Banco de dados gerenciado
- **Exemplo:** Azure SQL Database
- **Quando usar:** Dados estruturados da aplicação

### 4. Containers
- **O que é:** Aplicação empacotada com dependências
- **Exemplo:** Docker no Azure
- **Quando usar:** Deploy consistente, microservices

---

## 💰 Como Funciona o Pagamento?

### Pay-as-you-go (Pague pelo uso)
**Como funciona:**
- VM ligada 1 hora = paga 1 hora
- VM desligada = não paga (só o disco)

**Exemplo real:**
- VM B1s: ~R$ 0,04/hora
- Ligada 24/7 por mês: ~R$ 30
- Ligada 8h/dia útil: ~R$ 7

💡 **Dica:** Sempre desligue quando não estiver usando!

---

## 📍 Regiões

**O que são:** Locais físicos dos datacenters

**Azure no Brasil:**
- 🇧🇷 Brazil South (São Paulo)
- 🇧🇷 Brazil Southeast (Rio de Janeiro)

**Por que importa:**
- Mais perto = mais rápido (menor latência)
- LGPD: dados de brasileiros devem ficar no Brasil
- Preço varia por região

---

## 🔒 Segurança: Quem Cuida do Quê?

### Você Cuida:
- ✅ Suas senhas
- ✅ Quem acessa o quê
- ✅ Dados da aplicação
- ✅ Sistema operacional (no IaaS)

### Azure Cuida:
- ✅ Segurança física do datacenter
- ✅ Hardware
- ✅ Rede física

💡 **Regra de ouro:** Use senhas fortes e não compartilhe credenciais!

---

## 🎓 Exercícios Rápidos

### Exercício 1: IaaS, PaaS ou SaaS?
1. Gmail → ?
2. Azure Virtual Machine → ?
3. Heroku (deploy de app) → ?

<details>
<summary>Respostas</summary>

1. Gmail → **SaaS** (software pronto)
2. Azure Virtual Machine → **IaaS** (você gerencia tudo)
3. Heroku → **PaaS** (foca no código)
</details>

---

### Exercício 2: Quando usar Cloud?
Marque as situações onde cloud faz sentido:

- [ ] A) Site que pode ter 10 ou 10 milhões de acessos
- [ ] B) Aplicação crítica que não pode sair do ar
- [ ] C) Guardar backup de fotos
- [ ] D) Todas as anteriores

<details>
<summary>Resposta</summary>

**D) Todas as anteriores!**
- A) Cloud escala automaticamente
- B) Cloud tem alta disponibilidade
- C) Storage é perfeito para backups
</details>

---

## 🚀 Próximos Passos Práticos

Agora que você sabe a teoria, vamos praticar:

### 1. Azure Storage Account (1h)
- Criar uma conta de armazenamento
- Fazer upload de arquivos
- Hospedar um site estático

👉 **[Ir para o exercício](../azure/storage/README.md)**

---

### 2. Azure Virtual Machine (1h30)
- Criar uma VM Ubuntu
- Conectar via SSH
- Instalar Docker

👉 **[Ir para o exercício](../azure/vm/README.md)**

---

### 3. Deploy Docker na Cloud (1h)
- Rodar container Docker na VM
- Expor aplicação na internet
- Gerenciar a aplicação

👉 **[Ver exercícios práticos](../azure/vm/README.md#exercícios-práticos)**

---

## 📖 Resumo - Conceitos Essenciais

**Para a prova/trabalho, lembre-se:**

1. ☁️ **Cloud** = recursos de TI pela internet, pague pelo uso
2. 🏗️ **IaaS** = você gerencia tudo; **PaaS** = gerencia app; **SaaS** = só usa
3. 💰 **Custo** = paga por hora de uso, desligue quando não usar
4. 🌍 **Região** = onde os servidores estão fisicamente
5. 🔒 **Segurança** = compartilhada entre você e o provedor

---

## ❓ Perguntas Frequentes

**P: Cloud é sempre mais barato?**
R: Depende! Para pequena escala e uso sob demanda, sim. Para uso 24/7 constante, às vezes servidor próprio compensa.

**P: Meus dados ficam seguros?**
R: Sim! Azure tem certificações (ISO, SOC) e criptografia. Mas VOCÊ precisa usar boas práticas (senhas fortes, MFA).

**P: Preciso de internet o tempo todo?**
R: Para acessar recursos da cloud, sim. Mas existem estratégias de cache/offline.

**P: Posso migrar para outra cloud depois?**
R: Sim, mas dá trabalho. Por isso, use padrões abertos quando possível (Docker, Kubernetes).

---

**⏱️ Tempo de leitura:** ~30 minutos

**🎯 Próximo passo:** [Criar sua primeira VM no Azure](../azure/vm/README.md)

---

**Feito com 💙 pela equipe [ToolBox Technology](https://tbxtech.com.br/)**
