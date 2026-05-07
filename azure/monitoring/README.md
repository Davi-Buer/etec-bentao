# 📊 Application Insights + Log Analytics - Monitoramento

Monitore e analise o desempenho das suas aplicações em tempo real!

## 📚 O que você vai aprender

- O que é Application Insights
- O que é Log Analytics Workspace
- Monitorar aplicações web
- Ver métricas e logs
- Detectar problemas de performance

---

## 🎯 O que são esses serviços?

### Application Insights
**Monitora aplicações web e APIs**

**O que ele faz:**
- 📈 Rastreia requisições HTTP
- ⚡ Mede tempo de resposta
- 🐛 Detecta erros e exceções
- 👥 Conta usuários ativos
- 🌍 Mapeia requisições por localização

**Quando usar:**
- Monitorar App Service
- Detectar gargalos de performance
- Ver quais páginas são mais acessadas

---

### Log Analytics Workspace
**Armazena e analisa logs de múltiplos serviços**

**O que ele faz:**
- 📝 Centraliza logs de VMs, App Services, etc
- 🔍 Permite consultas (queries) em logs
- 📊 Cria dashboards customizados
- 🚨 Configura alertas

**Quando usar:**
- Centralizar logs de vários recursos
- Fazer análises complexas
- Debugging avançado

---

## 🚀 Parte 1: Application Insights para App Service

### Passo 1: Habilitar Application Insights

**Opção A: Durante criação do App Service**
1. Ao criar App Service, na aba "Monitoring"
2. Habilite "Application Insights" = **Yes**
3. Ele criará automaticamente!

**Opção B: App Service existente**
1. Vá no seu App Service
2. No menu, procure "Application Insights"
3. Clique em "Turn on Application Insights"
4. "Create new" ou use existente
5. Clique em "Apply"

💡 **É automático!** Não precisa modificar código para métricas básicas.

---

### Passo 2: Ver Métricas

**1. Vá no App Service → "Application Insights"**

**2. Clique em "View Application Insights data"**

**3. Explore:**

#### **Métricas Disponíveis:**
- **Server requests** - Número de requisições
- **Server response time** - Tempo médio de resposta
- **Failed requests** - Requisições com erro
- **Page views** - Visualizações de página
- **Users** - Usuários únicos
- **Sessions** - Sessões ativas

---

### Passo 3: Ver Logs

**1. No Application Insights, vá em "Logs"**

**2. Exemplos de queries:**

**Ver últimas requisições:**
```kusto
requests
| where timestamp > ago(1h)
| order by timestamp desc
| take 20
```

**Ver requisições lentas (> 1 segundo):**
```kusto
requests
| where duration > 1000
| order by duration desc
```

**Ver erros (status 500):**
```kusto
requests
| where resultCode == "500"
| order by timestamp desc
```

**Contar requisições por URL:**
```kusto
requests
| summarize count() by url
| order by count_ desc
```

---

## 🔧 Parte 2: Instrumentação Customizada (Opcional)

### Node.js - Enviar Eventos Customizados

**1. Instalar biblioteca:**
```bash
npm install applicationinsights
```

**2. Configurar no código:**
```javascript
const appInsights = require("applicationinsights");

// Connection string do Application Insights
// (encontre em: App Insights → Overview → Connection String)
appInsights.setup("InstrumentationKey=abc-123-xyz...")
  .setAutoDependencyCorrelation(true)
  .setAutoCollectRequests(true)
  .setAutoCollectPerformance(true, true)
  .setAutoCollectExceptions(true)
  .setAutoCollectDependencies(true)
  .setAutoCollectConsole(true)
  .start();

const client = appInsights.defaultClient;

// Rastrear evento customizado
client.trackEvent({ name: "UserLogin", properties: { userId: "123" } });

// Rastrear métrica customizada
client.trackMetric({ name: "TempoProcessamento", value: 250 });

// Rastrear exceção
try {
  // código que pode falhar
} catch (error) {
  client.trackException({ exception: error });
}
```

---

## 📊 Parte 3: Log Analytics Workspace

### Criar Log Analytics Workspace

**Via Portal:**
1. Pesquise "Log Analytics workspaces"
2. Clique em "+ Create"
3. Preencha:
   - Resource group: `rg-aluno-SEUNOME`
   - Name: `law-aluno-SEUNOME`
   - Region: `Brazil South`
4. Review + create

**Via CLI:**
```bash
az monitor log-analytics workspace create \
  --resource-group rg-aluno-SEUNOME \
  --workspace-name law-aluno-SEUNOME \
  --location brazilsouth
```

---

### Conectar Recursos ao Log Analytics

**Para VM:**
1. Vá na VM → "Insights"
2. Clique em "Enable"
3. Selecione o Log Analytics Workspace
4. Aguarde instalação do agente

**Para App Service:**
- Application Insights já envia dados automaticamente se criado junto com workspace

---

### Queries Úteis

**Ver logs de uma VM:**
```kusto
Syslog
| where Computer == "vm-aluno-joao"
| order by TimeGenerated desc
| take 50
```

**Ver uso de CPU:**
```kusto
Perf
| where ObjectName == "Processor"
| where CounterName == "% Processor Time"
| summarize avg(CounterValue) by bin(TimeGenerated, 5m), Computer
| render timechart
```

**Ver erros de aplicações:**
```kusto
AppExceptions
| where TimeGenerated > ago(24h)
| summarize count() by ProblemId
| order by count_ desc
```

---

## 🚨 Parte 4: Alertas

### Criar Alerta de Performance

**1. No App Service ou App Insights, vá em "Alerts"**

**2. Clique em "+ Create" → "Alert rule"**

**3. Configure:**

**Condition:**
- Signal: `Server response time`
- Threshold: `>` `2 seconds`
- Evaluation period: `5 minutes`

**Actions:**
- Create action group
- Nome: `alerta-performance`
- Notification: Email para você

**Details:**
- Alert rule name: `Alerta Tempo de Resposta Alto`
- Severity: `2 - Warning`

**4. Review + create**

---

### Tipos de Alertas Úteis

| Alerta | Quando dispara | Threshold |
|--------|----------------|-----------|
| **Tempo de resposta** | App lento | > 2 segundos |
| **Taxa de erro** | Muitos erros | > 5% das requisições |
| **CPU alta** | VM sobrecarregada | > 80% por 10 min |
| **Memória alta** | Vazamento de memória | > 90% por 5 min |
| **Disco cheio** | Sem espaço | > 90% usado |

---

## 📈 Parte 5: Dashboards

### Criar Dashboard Customizado

**1. No Portal Azure, clique em "Dashboard" (topo)**

**2. Clique em "+ New dashboard"**

**3. Nome: `Dashboard Aluno SEUNOME`**

**4. Arraste tiles úteis:**
- **Metrics chart** → Adicione CPU da VM
- **Logs** → Adicione query de requisições
- **Alerts** → Mostre alertas ativos

**5. Clique em "Done customizing"**

---

## 📝 Exercícios Práticos

### Exercício 1: Habilitar Monitoramento
1. ✅ Habilite Application Insights no seu App Service
2. ✅ Acesse o app algumas vezes
3. ✅ Veja as métricas no Application Insights
4. ✅ Tire um print das métricas

### Exercício 2: Análise de Logs
1. ✅ Vá em "Logs" no Application Insights
2. ✅ Execute a query para ver últimas requisições
3. ✅ Modifique para ver apenas as últimas 5
4. ✅ Tire um print dos resultados

### Exercício 3: Criar Alerta
1. ✅ Crie um alerta de tempo de resposta alto
2. ✅ Configure para enviar email para você
3. ✅ Faça requisições lentas no app (adicione `sleep()`)
4. ✅ Veja se recebe o email de alerta

### Exercício 4: Dashboard
1. ✅ Crie um dashboard
2. ✅ Adicione gráfico de requisições/minuto
3. ✅ Adicione gráfico de tempo de resposta
4. ✅ Pin o dashboard como favorito

---

## 🆘 Problemas Comuns

### Não vejo dados no Application Insights
→ **Soluções:**
1. Aguarde 5-10 minutos (dados levam tempo)
2. Acesse a aplicação para gerar tráfego
3. Verifique se Application Insights está habilitado
4. Veja logs de erro do App Service

### Query não funciona
→ **Soluções:**
1. Verifique sintaxe Kusto (case-sensitive!)
2. Verifique se há dados no período selecionado
3. Use o autocompletar (Ctrl+Space)

---

## 💰 Custos

**Application Insights:**
- Primeiros 5 GB/mês: **Grátis**
- Depois: ~R$ 10/GB
- App pequeno: geralmente gratuito!

**Log Analytics Workspace:**
- Primeiros 5 GB/mês: **Grátis**
- Depois: ~R$ 12/GB

💡 **Para aprendizado:** Provavelmente ficará no tier gratuito!

---

## 📊 Quando Usar Cada Um?

| Preciso... | Use |
|-----------|-----|
| Monitorar App Service | Application Insights |
| Centralizar logs de várias VMs | Log Analytics |
| Ver performance de API | Application Insights |
| Queries complexas em logs | Log Analytics |
| Alertas simples | Application Insights |
| Alertas complexos | Log Analytics + Alertas |

---

## 🎓 Linguagem Kusto (KQL)

### Comandos Básicos

```kusto
// Ver últimos registros
requests
| take 10

// Filtrar por tempo
requests
| where timestamp > ago(1h)

// Ordenar
requests
| order by duration desc

// Contar
requests
| summarize count() by resultCode

// Filtrar e contar
requests
| where duration > 1000
| summarize count()

// Criar gráfico
requests
| summarize count() by bin(timestamp, 5m)
| render timechart
```

---

## 🔗 Integrações Úteis

### Application Insights + App Service
- Automático, só habilitar!

### Log Analytics + VM
- Instale o agente de monitoramento
- Veja Syslog, Performance, Heartbeat

### Alertas + Email/SMS
- Receba notificação quando algo der errado

### Power BI
- Exporte dados para dashboards avançados

---

## 📖 Recursos Adicionais

- [Documentação Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview)
- [Documentação Log Analytics](https://docs.microsoft.com/azure/azure-monitor/logs/log-analytics-overview)
- [Exemplos de Queries KQL](https://docs.microsoft.com/azure/data-explorer/kusto/query/)
- [Tutorial Interativo KQL](https://docs.microsoft.com/azure/data-explorer/kusto/query/tutorial)

---

## 📊 Resumo

**Application Insights:**
- 📱 Monitora aplicações
- ⚡ Performance e erros
- 👥 Usuários e sessões

**Log Analytics:**
- 📝 Centraliza logs
- 🔍 Queries avançadas (KQL)
- 📊 Dashboards customizados

**Use ambos para monitoramento completo!**

---

**Dúvidas?** Pergunte ao seu instrutor! 🙋

**Feito com 💙 pela equipe [ToolBox Technology](https://tbxtech.com.br/)**
