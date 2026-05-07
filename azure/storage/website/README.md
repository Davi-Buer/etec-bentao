# 🌐 Hospedagem de Site Estático no Azure Storage

Guia completo para hospedar seu próprio site usando Azure Storage Account.

## 🎯 O que é Static Website Hosting?

É um recurso do Azure Storage que permite hospedar sites HTML/CSS/JS **sem precisar de servidor**!

**Vantagens:**
- ⚡ Super rápido
- 💰 Muito barato (centavos por mês)
- 🚀 Fácil de configurar
- 🌍 Acesso global
- 📈 Escalável automaticamente

**Ideal para:**
- Sites pessoais
- Portfólios
- Páginas de eventos
- Landing pages
- Documentação
- Blogs estáticos

---

## 📋 Pré-requisitos

1. Um Storage Account criado no Azure (veja `../README.md` se ainda não criou)
2. Os arquivos HTML do site (já incluídos nesta pasta!)

---

## 🚀 Parte 1: Habilitar Static Website

**1. Acesse seu Storage Account no Portal Azure**

**2. No menu lateral, procure por "Static website"**
   - Pode estar em **"Data management"** ou **"Settings"**

**3. Configure o Static Website:**

| Campo | Valor |
|-------|-------|
| **Static website** | Enabled (habilitado) ✅ |
| **Index document name** | `index.html` |
| **Error document path** | `404.html` (opcional) |

4. Clique em **"Save"** (Salvar)

**5. Copie a URL do site:**
   - Após salvar, aparecerá a **Primary endpoint**
   - Algo como: `https://stalgseunome.z15.web.core.windows.net/`
   - 🔖 Salve essa URL! É o endereço do seu site!

⚠️ **IMPORTANTE:** Um novo container chamado `$web` foi criado automaticamente!

---

## 📤 Parte 2: Fazer Upload dos Arquivos

### Opção A: Via Portal Azure (Mais Fácil)

1. No seu Storage Account, vá em **"Containers"**
2. Clique no container **"$web"**
3. Clique em **"Upload"**
4. Selecione **todos** os arquivos do site:
   - `index.html`
   - `style.css`
   - `script.js`
5. Clique em **"Upload"**

✅ Pronto! Acesse a URL do seu site!

### Opção B: Via Script Python

```bash
# Volte para a pasta principal
cd ..

# Configure o .env se ainda não fez
cp .env.example .env
nano .env

# Use o script de upload
python upload_website.py
```

### Opção C: Via Azure CLI

```bash
# Configure a variável de ambiente
export AZURE_STORAGE_CONNECTION_STRING="sua-connection-string"

# Faça upload de todos os arquivos
az storage blob upload-batch \
  --source ./website \
  --destination '$web' \
  --connection-string "$AZURE_STORAGE_CONNECTION_STRING"
```

---

## 🎨 Parte 3: Personalizar o Site

**1. Edite o `index.html`:**

Encontre esta linha:
```html
<p>🎓 Criado por: <span class="destaque">[SEU NOME AQUI]</span></p>
```

Mude para seu nome:
```html
<p>🎓 Criado por: <span class="destaque">João Silva</span></p>
```

**2. Personalize as cores (`style.css`):**

Encontre as cores principais:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

Mude para suas cores favoritas! Alguns exemplos:

```css
/* Verde/Azul */
background: linear-gradient(135deg, #0ba360 0%, #3cba92 100%);

/* Laranja/Vermelho */
background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);

/* Roxo/Rosa */
background: linear-gradient(135deg, #c471f5 0%, #fa71cd 100%);
```

**3. Adicione mais conteúdo:**

Você pode adicionar novas seções, imagens, links, etc!

**4. Faça upload novamente:**

Depois de editar, faça upload dos arquivos modificados novamente (eles serão substituídos).

---

## 🎯 Exercícios Práticos

### Exercício 1: Primeiro Deploy
1. Habilite o Static Website no seu Storage Account
2. Faça upload dos 3 arquivos (HTML, CSS, JS)
3. Acesse a URL do site
4. Tire um print e compartilhe com a turma!

### Exercício 2: Personalização Básica
1. Mude o título do site no HTML
2. Coloque seu nome no footer
3. Faça upload novamente
4. Atualize a página (F5) e veja as mudanças

### Exercício 3: Mudança de Cores
1. Escolha 2 cores no [coolors.co](https://coolors.co)
2. Mude o gradiente do fundo no CSS
3. Faça upload do `style.css` modificado
4. Veja como o site mudou!

### Exercício 4: Adicionar uma Foto
1. Escolha uma imagem (pode ser seu logo ou foto)
2. Renomeie para `logo.png` ou `logo.jpg`
3. Faça upload para o container `$web`
4. No HTML, adicione:
   ```html
   <img src="logo.png" alt="Meu Logo" style="width: 200px;">
   ```
5. Atualize e veja sua imagem!

### Exercício 5: Desafio - Criar uma Nova Página
1. Crie um arquivo `sobre.html`
2. Copie a estrutura do `index.html`
3. Mude o conteúdo para falar sobre você
4. No `index.html`, adicione um link:
   ```html
   <a href="sobre.html" class="btn">Sobre Mim</a>
   ```
5. Faça upload de ambos os arquivos

---

## 🔍 Testando o Site

### Verificar se está online:
```bash
# Usando curl
curl https://SEUSITE.z15.web.core.windows.net/

# Deve retornar o HTML completo
```

### Testar performance:
1. Abra o site no navegador
2. Pressione F12 (DevTools)
3. Vá na aba **"Network"**
4. Recarregue a página (F5)
5. Veja o tempo de carregamento! ⚡

---

## 📱 Compartilhar o Site

Agora você tem um site público! Compartilhe com:

- 👨‍👩‍👧‍👦 Família e amigos
- 📱 Redes sociais
- 🎓 Colegas da escola
- 💼 Portfólio profissional

**Dicas para compartilhar:**
- Encurte a URL com [bit.ly](https://bitly.com)
- Crie um QR Code no [qr-code-generator.com](https://www.qr-code-generator.com/)
- Adicione ao seu perfil do LinkedIn ou GitHub

---

## 🛠️ Comandos Úteis

### Ver todos os arquivos no $web:
```bash
az storage blob list \
  --container-name '$web' \
  --connection-string "$AZURE_STORAGE_CONNECTION_STRING" \
  --output table
```

### Deletar um arquivo específico:
```bash
az storage blob delete \
  --container-name '$web' \
  --name index.html \
  --connection-string "$AZURE_STORAGE_CONNECTION_STRING"
```

### Download de backup do site:
```bash
az storage blob download-batch \
  --source '$web' \
  --destination ./backup \
  --connection-string "$AZURE_STORAGE_CONNECTION_STRING"
```

---

## 🎨 Recursos para Aprender Mais

### HTML/CSS/JavaScript:
- [MDN Web Docs](https://developer.mozilla.org/pt-BR/) - Documentação completa
- [W3Schools](https://www.w3schools.com/) - Tutoriais interativos
- [FreeCodeCamp](https://www.freecodecamp.org/) - Cursos gratuitos

### Design:
- [Coolors](https://coolors.co/) - Paletas de cores
- [Google Fonts](https://fonts.google.com/) - Fontes gratuitas
- [Font Awesome](https://fontawesome.com/) - Ícones grátis
- [Unsplash](https://unsplash.com/) - Fotos gratuitas

### Templates Prontos:
- [HTML5 UP](https://html5up.net/) - Templates responsivos
- [Start Bootstrap](https://startbootstrap.com/) - Templates Bootstrap

---

## 🆘 Problemas Comuns

### Site não aparece (404)
→ Verifique se:
1. Static website está **Enabled**
2. O arquivo se chama exatamente `index.html` (minúsculas!)
3. O arquivo está no container `$web` (não em outro!)
4. Aguarde 1-2 minutos após o upload

### CSS não carrega (site sem estilo)
→ Verifique se:
1. O arquivo `style.css` foi enviado para `$web`
2. O nome está correto no HTML: `<link rel="stylesheet" href="style.css">`
3. Limpe o cache do navegador (Ctrl + F5)

### JavaScript não funciona
→ Verifique se:
1. O arquivo `script.js` foi enviado para `$web`
2. O console do navegador (F12) mostra algum erro
3. O nome está correto no HTML: `<script src="script.js"></script>`

### Mudanças não aparecem
→ Soluções:
1. Limpe o cache: Ctrl + Shift + R (Windows) ou Cmd + Shift + R (Mac)
2. Abra em aba anônima/privada
3. Aguarde alguns segundos (pode ter cache do Azure)

---

## 🌟 Próximos Passos

Depois de dominar o básico, você pode:

1. **Adicionar um domínio personalizado**
   - Em vez de `...web.core.windows.net`
   - Use `www.seunome.com.br`

2. **Adicionar HTTPS customizado**
   - Certificado SSL gratuito
   - Via Azure CDN

3. **Integrar com GitHub Actions**
   - Deploy automático ao fazer push
   - CI/CD para seu site!

4. **Adicionar analytics**
   - Google Analytics
   - Microsoft Clarity

5. **Usar um framework**
   - React
   - Vue.js
   - Next.js (static export)

---

## 📊 Estrutura dos Arquivos

```
website/
├── index.html          # Página principal do site
├── style.css          # Estilos e design
├── script.js          # Interatividade
└── README.md          # Este guia
```

---

## 💡 Dica Pro

Crie um arquivo `404.html` para quando alguém acessar uma página que não existe:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Página não encontrada</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>404 - Página não encontrada 😢</h1>
        <p>A página que você procura não existe.</p>
        <a href="/" class="btn">Voltar para o início</a>
    </div>
</body>
</html>
```

---

**Dúvidas?** Pergunte ao seu instrutor! 🙋

**Gostou?** Compartilhe seu site com a turma! 🎉
