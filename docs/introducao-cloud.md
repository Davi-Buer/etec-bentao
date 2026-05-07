# ☁️ Introdução a Cloud Computing

Um guia completo sobre conceitos de computação em nuvem para iniciantes.

## 📚 O que é Cloud Computing (Computação em Nuvem)?

**Definição simples:**
Cloud Computing é usar recursos de computação (servidores, armazenamento, bancos de dados, software) pela internet, pagando apenas pelo que você usa.

**Analogia:**
- **Antes:** Você compra um gerador para ter energia em casa
- **Cloud:** Você usa a energia da rede elétrica e paga apenas o que consome

---

## 🎯 Por que usar Cloud?

### Vantagens

| Vantagem | Explicação | Exemplo |
|----------|------------|---------|
| 💰 **Custo** | Pague apenas pelo que usar | Netflix paga por streaming, não por servidores parados |
| 📈 **Escalabilidade** | Aumente ou diminua recursos sob demanda | Black Friday: mais servidores; Janeiro: menos servidores |
| 🌍 **Disponibilidade Global** | Seus serviços em múltiplos países | Site brasileiro acessível na Europa |
| ⚡ **Velocidade** | Configure recursos em minutos | VM criada em 5 min vs. comprar servidor físico (semanas) |
| 🔧 **Menos Manutenção** | Provedor cuida do hardware | Não precisa trocar HD queimado |
| 🔄 **Backup Automático** | Redundância integrada | Dados replicados em múltiplos datacenters |

### Desvantagens

| Desvantagem | Explicação | Mitigação |
|-------------|------------|-----------|
| 📶 **Dependência de Internet** | Precisa de conexão | Ter plano B de internet |
| 🔒 **Segurança** | Dados em servidores de terceiros | Criptografia e conformidade |
| 💸 **Custos Inesperados** | Má gestão pode sair caro | Monitoramento e alertas |
| 🏢 **Vendor Lock-in** | Difícil migrar entre clouds | Usar padrões abertos |

---

## 🏗️ Modelos de Serviço Cloud

### 1. IaaS - Infrastructure as a Service
**"Você aluga a infraestrutura"**

**O que você ganha:**
- Máquinas virtuais
- Redes
- Armazenamento

**Você gerencia:**
- Sistema operacional
- Aplicações
- Dados

**Exemplos:**
- ☁️ Azure Virtual Machines
- 🌐 Google Compute Engine
- 📦 AWS EC2

**Quando usar:**
- Você quer controle total
- Migração de servidores físicos (lift and shift)
- Ambiente de desenvolvimento/teste

---

### 2. PaaS - Platform as a Service
**"Você só se preocupa com a aplicação"**

**O que você ganha:**
- IaaS +
- Sistema operacional configurado
- Runtime de linguagem
- Banco de dados

**Você gerencia:**
- Sua aplicação
- Seus dados

**Exemplos:**
- ☁️ Azure App Service
- 🌐 Google App Engine
- 🐳 Heroku

**Quando usar:**
- Focar no desenvolvimento
- Não quer gerenciar infraestrutura
- Prototipagem rápida

---

### 3. SaaS - Software as a Service
**"Você só usa o software"**

**O que você ganha:**
- Tudo! Software pronto para usar

**Você gerencia:**
- Seus dados e configurações

**Exemplos:**
- 📧 Gmail
- 💼 Microsoft 365
- 📊 Salesforce
- 💬 Slack

**Quando usar:**
- Sempre que possível!
- Não quer instalar/manter software
- Colaboração em equipe

---

## 📊 Comparação dos Modelos

```
          Você        |      Provedor
          gerencia    |      gerencia
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                      |
On-Premises (Local)   |
                      |
Aplicações       ✅   |
Dados            ✅   |
Runtime          ✅   |
Sistema Op.      ✅   |
Virtualização    ✅   |
Servidores       ✅   |
Armazenamento    ✅   |
Rede             ✅   |
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                      |
IaaS                  |
                      |
Aplicações       ✅   |
Dados            ✅   |
Runtime          ✅   |
Sistema Op.      ✅   |
Virtualização         |   ✅
Servidores            |   ✅
Armazenamento         |   ✅
Rede                  |   ✅
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                      |
PaaS                  |
                      |
Aplicações       ✅   |
Dados            ✅   |
Runtime               |   ✅
Sistema Op.           |   ✅
Virtualização         |   ✅
Servidores            |   ✅
Armazenamento         |   ✅
Rede                  |   ✅
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                      |
SaaS                  |
                      |
Aplicações            |   ✅
Dados            ✅   |
Runtime               |   ✅
Sistema Op.           |   ✅
Virtualização         |   ✅
Servidores            |   ✅
Armazenamento         |   ✅
Rede                  |   ✅
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🌍 Tipos de Cloud

### 1. Cloud Pública
**Recursos compartilhados com outros clientes**

**Características:**
- ✅ Mais barato
- ✅ Escalável
- ✅ Sem manutenção
- ❌ Menos controle

**Exemplos:** Azure, Google Cloud, AWS

**Quando usar:** Maioria dos casos

---

### 2. Cloud Privada
**Infraestrutura dedicada exclusivamente para você**

**Características:**
- ✅ Mais controle
- ✅ Mais segurança
- ❌ Mais caro
- ❌ Você gerencia

**Exemplos:** VMware, OpenStack no seu datacenter

**Quando usar:** 
- Requisitos regulatórios rígidos
- Dados ultra-sensíveis

---

### 3. Cloud Híbrida
**Mistura de cloud pública + privada**

**Características:**
- ✅ Flexibilidade
- ✅ Otimização de custos
- ✅ Gradual
- ❌ Mais complexo

**Exemplo:** 
- Banco de dados sensível: privada
- Frontend: pública

**Quando usar:** Transição gradual para cloud

---

## 🏢 Principais Provedores de Cloud

### Microsoft Azure
- ☁️ **Forte em:** Integração com Windows, Office 365
- 🌍 **Presença:** 60+ regiões
- 💼 **Ideal para:** Empresas que já usam Microsoft

### Google Cloud Platform (GCP)
- 🔍 **Forte em:** Big Data, Machine Learning, Kubernetes
- 🌍 **Presença:** 35+ regiões
- 💼 **Ideal para:** Análise de dados, AI/ML

### Amazon Web Services (AWS)
- 👑 **Líder de mercado** (33% de participação)
- 🌍 **Presença:** 30+ regiões
- 💼 **Ideal para:** Maior variedade de serviços

### Outros
- 🇨🇳 **Alibaba Cloud:** Forte na Ásia
- 🇺🇸 **Oracle Cloud:** Forte em banco de dados
- 🇺🇸 **IBM Cloud:** Forte em mainframe/enterprise

---

## 🛠️ Tipos de Recursos em Cloud

### Computação (Compute)
**Processamento / VMs / Containers**

| Serviço | Azure | Google Cloud | AWS |
|---------|-------|--------------|-----|
| VMs | Virtual Machines | Compute Engine | EC2 |
| Containers | Container Instances | Cloud Run | ECS |
| Kubernetes | AKS | GKE | EKS |
| Serverless | Functions | Cloud Functions | Lambda |

---

### Armazenamento (Storage)
**Guardar arquivos / Dados**

| Tipo | Azure | Google Cloud | AWS |
|------|-------|--------------|-----|
| Object Storage | Blob Storage | Cloud Storage | S3 |
| File Storage | Files | Filestore | EFS |
| Block Storage | Managed Disks | Persistent Disk | EBS |

---

### Banco de Dados (Database)
**Dados estruturados**

| Tipo | Azure | Google Cloud | AWS |
|------|-------|--------------|-----|
| SQL | SQL Database | Cloud SQL | RDS |
| NoSQL | Cosmos DB | Firestore | DynamoDB |
| Cache | Cache for Redis | Memorystore | ElastiCache |

---

### Redes (Networking)
**Comunicação entre recursos**

| Serviço | Descrição |
|---------|-----------|
| Virtual Network | Rede isolada na cloud |
| Load Balancer | Distribui tráfego entre VMs |
| CDN | Conteúdo mais perto do usuário |
| DNS | Traduz domínio → IP |

---

### Segurança e Identidade

| Serviço | Descrição |
|---------|-----------|
| IAM | Gerenciamento de permissões |
| Key Vault | Guardar senhas/chaves |
| Firewall | Proteção de rede |
| DDoS Protection | Proteção contra ataques |

---

## 💰 Modelos de Pagamento

### Pay-as-you-go (Pague pelo uso)
- 💵 **Como funciona:** Paga por hora/minuto de uso
- ✅ **Vantagem:** Flexível, sem compromisso
- ❌ **Desvantagem:** Pode ser mais caro

**Exemplo:** VM ligada 100 horas = paga 100 horas

---

### Reserved Instances (Instâncias Reservadas)
- 💵 **Como funciona:** Compromisso de 1-3 anos
- ✅ **Vantagem:** Até 70% mais barato
- ❌ **Desvantagem:** Tem que pagar mesmo sem usar

**Exemplo:** Reserva VM por 1 ano = desconto grande

---

### Spot/Preemptible (Instâncias Spot)
- 💵 **Como funciona:** Usa capacidade ociosa do provedor
- ✅ **Vantagem:** Até 90% mais barato
- ❌ **Desvantagem:** Pode ser desligada a qualquer momento

**Exemplo:** Processamento de vídeo não-urgente

---

## 📈 Conceitos Importantes

### Elasticidade
**Capacidade de aumentar/diminuir recursos automaticamente**

**Exemplo:**
- Site de notícias: tráfego alto de manhã, baixo à noite
- Cloud aumenta VMs às 8h, diminui às 20h
- Você paga apenas o necessário

---

### Alta Disponibilidade (High Availability)
**Sistema continua funcionando mesmo com falhas**

**Como funciona:**
- Recursos duplicados em múltiplos datacenters
- Se um falha, outro assume

**Medida:** SLA (Service Level Agreement)
- 99% = ~7h downtime/mês
- 99.9% = ~43min downtime/mês
- 99.99% = ~4min downtime/mês

---

### Recuperação de Desastres (Disaster Recovery)
**Plano para recuperar dados após catástrofe**

**Estratégias:**
1. **Backup:** Cópias regulares dos dados
2. **Replicação:** Dados em múltiplas regiões
3. **Snapshot:** "Foto" do estado do sistema

---

### Regiões e Zonas

**Região (Region):**
- Área geográfica com datacenters
- Exemplo: Brazil South (São Paulo)

**Zona de Disponibilidade (Availability Zone):**
- Datacenters separados fisicamente dentro de uma região
- Protege contra falha de um datacenter

**Como escolher região:**
- ✅ Mais perto dos usuários = menor latência
- ✅ Conformidade legal (LGPD no Brasil)
- ✅ Custo (varia por região)

---

## 🔒 Segurança na Cloud

### Modelo de Responsabilidade Compartilhada

```
┌─────────────────────────────────────┐
│  SUA RESPONSABILIDADE               │
├─────────────────────────────────────┤
│  • Dados                            │
│  • Identidades e acessos            │
│  • Aplicações                       │
│  • Sistema Operacional (IaaS)       │
└─────────────────────────────────────┘
         ↕️  COMPARTILHADO  ↕️
┌─────────────────────────────────────┐
│  RESPONSABILIDADE DO PROVEDOR       │
├─────────────────────────────────────┤
│  • Segurança física                 │
│  • Rede física                      │
│  • Hardware                         │
│  • Virtualização                    │
└─────────────────────────────────────┘
```

---

### Melhores Práticas

1. **Princípio do Menor Privilégio**
   - Dê apenas as permissões necessárias
   - Exemplo: Dev não precisa deletar banco de produção

2. **Multi-Factor Authentication (MFA)**
   - Senha + código do celular
   - Muito mais seguro

3. **Criptografia**
   - Dados em trânsito (HTTPS)
   - Dados em repouso (disco criptografado)

4. **Auditoria**
   - Logs de quem acessou o quê
   - Detectar atividades suspeitas

---

## 🎓 Casos de Uso Reais

### Startup de Aplicativo
**Problema:** Não sabe quantos usuários terá

**Solução Cloud:**
- Começa pequeno (1 VM pequena)
- App faz sucesso? Escala automaticamente
- Usuários caem? Diminui recursos
- **Resultado:** Paga apenas o que usa

---

### E-commerce
**Problema:** Black Friday tem 100x mais acessos

**Solução Cloud:**
- Novembro normal: 5 VMs
- Black Friday: 100 VMs
- Dezembro: volta para 5 VMs
- **Resultado:** Não precisa manter 100 VMs o ano todo

---

### Escola/Universidade
**Problema:** Período de matrícula sobrecarrega sistema

**Solução Cloud:**
- Durante o ano: recursos normais
- Período de matrícula: aumenta capacidade
- Backup automático de dados de alunos
- **Resultado:** Sistema nunca cai nas matrículas

---

## 📚 Exercícios Práticos

### Exercício 1: Identificar Tipo de Cloud
Classifique como IaaS, PaaS ou SaaS:
1. Netflix → ?
2. Azure Virtual Machine → ?
3. Google Docs → ?
4. Heroku (deploy de app) → ?

<details>
<summary>Ver respostas</summary>

1. Netflix → SaaS
2. Azure Virtual Machine → IaaS
3. Google Docs → SaaS
4. Heroku → PaaS
</details>

---

### Exercício 2: Escolher Solução
Para cada cenário, escolha a melhor solução:

**Cenário A:** Preciso hospedar um site WordPress
- [ ] Comprar servidor físico
- [ ] VM na cloud (IaaS)
- [ ] WordPress.com (SaaS)

**Cenário B:** Estou criando um app inovador e posso ter 10 ou 10 milhões de usuários
- [ ] Comprar servidor físico
- [ ] Cloud escalável
- [ ] Servidor VPS tradicional

<details>
<summary>Ver respostas</summary>

**A:** WordPress.com (SaaS) - mais simples, ou VM na cloud se quiser controle

**B:** Cloud escalável - única opção que escala de 10 para 10M
</details>

---

### Exercício 3: Calcular Economia
Uma VM B1s no Azure custa R$ 0,04/hora.

**Cenário 1:** VM ligada 24/7 por 30 dias
**Cenário 2:** VM ligada apenas 8h/dia útil (22 dias)

Calcule o custo de cada cenário.

<details>
<summary>Ver respostas</summary>

**Cenário 1:** 24h × 30 dias = 720h × R$ 0,04 = R$ 28,80

**Cenário 2:** 8h × 22 dias = 176h × R$ 0,04 = R$ 7,04

**Economia:** R$ 21,76 (75% mais barato!)
</details>

---

## 🔗 Próximos Passos

Agora que você entende os conceitos, pratique:

1. 🐳 **[Docker Compose](../README-docker.md)** - Containerização
2. ☁️ **[Azure Storage](../azure/storage/README.md)** - Armazenamento em nuvem
3. 🖥️ **[Azure VM](../azure/vm/README.md)** - Máquinas virtuais
4. 🌐 **[Static Website](../azure/storage/website/README.md)** - Hospedagem de sites

---

## 📖 Recursos Adicionais

### Certificações Gratuitas
- [Microsoft Learn](https://docs.microsoft.com/learn/) - Cursos gratuitos
- [Google Cloud Skills Boost](https://www.cloudskillsboost.google/) - Labs práticos
- [AWS Educate](https://aws.amazon.com/education/awseducate/) - Treinamento gratuito

### Calculadoras de Custo
- [Azure Pricing Calculator](https://azure.microsoft.com/pricing/calculator/)
- [GCP Pricing Calculator](https://cloud.google.com/products/calculator)
- [AWS Pricing Calculator](https://calculator.aws/)

### Glossário
- [Azure Glossary](https://docs.microsoft.com/azure/azure-glossary-cloud-terminology)
- [Cloud Computing Glossary](https://www.ibm.com/cloud/learn/cloud-computing-glossary)

---

**Feito com 💙 pela equipe [ToolBox Technology](https://tbxtech.com.br/)**
