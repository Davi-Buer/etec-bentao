# 🚦 Roteiro da aula — O que é DevOps & o conceito de CI/CD

Roteiro do **instrutor** para a aula de CI/CD. Os alunos usam **só o navegador**
(nada instalado): fork → editar um `.md` pela web → ver a Action rodar → abrir a
página no ar. O material da lição fica em [`cicd/`](cicd/).

> A página que o aluno lê durante a aula é o [`cicd/README.md`](cicd/README.md).
> Este roteiro é o guia de bastidores: critérios de aceite + como validar o repo
> antes da turma.

---

## 🎯 O que o aluno faz (os 5 passos)

Descritos em detalhe no [`cicd/README.md`](cicd/README.md):

1. **Fork** deste projeto para a conta dele.
2. **Ligar o robô** — aba `Actions` → "I understand my workflows, go ahead and enable them".
3. **Ligar a publicação** — `Settings` → `Pages` → **Source = GitHub Actions**.
4. **Escrever o arquivo** — `alunos/seunome.md` (minúsculo, sem espaço, sem acento).
5. **Ver o robô trabalhar** — 3 jobs em ordem, depois abrir o link do Pages.

Depois: **quebrar de propósito** (apagar a linha do título), ver o pipeline ficar
vermelho e o site **não** mudar, e então consertar e voltar ao verde.

---

## ✅ Critérios de aceite (o que o pipeline garante)

O job 1 (`scripts/check.py`) reprova o commit — **e o site não é publicado** — se
qualquer uma destas regras falhar:

1. **Nome do arquivo** só com `a-z`, `0-9`, `.`, `-` (sem espaço, sem acento, sem
   maiúscula). Regex: `[a-z0-9._-]+`.
2. **Primeira linha é o título**, começando com `# `.
3. **Há pelo menos uma linha** além do título.
4. A pasta `alunos/` **não pode estar vazia**.

Comportamento esperado do pipeline (é o coração da aula):

| Situação | Job 1 Verificar | Job 2 Construir | Job 3 Publicar | Site no ar |
|---|---|---|---|---|
| Arquivo válido | ✅ success | ✅ success | ✅ success | atualizado |
| Regra quebrada | ❌ **failure** | ⚪ **skipped** | ⚪ **skipped** | **inalterado** |

Os jobs 2 e 3 ficam **skipped** (cinza), **não** failed, porque encadeiam com
`needs:` (`construir needs verificar`, `publicar needs construir`). O deploy nem
roda → a versão que já estava em produção continua intacta. **Isso é integração
contínua: o erro para antes de chegar em alguém.**

Garantias de segurança do `scripts/build.py`: título e corpo passam por
`html.escape()`, então `<` e `&` viram texto literal — sem quebrar o HTML e sem
permitir injeção.

---

## 🗂️ Layout (importante)

A lição é um **projeto standalone**: no repo que o aluno forka, o conteúdo de
`cicd/` fica na **raiz** (`scripts/`, `alunos/`, `README.md`,
`.github/workflows/deploy.yml`). Por isso os scripts usam caminhos relativos
(`alunos/`, `scripts/...`) e o workflow vive em
[`cicd/.github/workflows/deploy.yml`](cicd/.github/workflows/deploy.yml) — assim
ele viaja junto com a lição e cai em `.github/workflows/` quando `cicd/` vira a
raiz do fork.

> ⚠️ Não coloque um `deploy.yml` na raiz **deste monorepo**: aqui `scripts/` e
> `alunos/` estão dentro de `cicd/`, e um workflow na raiz não acharia os
> arquivos.

Versões das actions (mantidas em tags de major, legíveis para os alunos):
`actions/checkout@v7`, `actions/upload-pages-artifact@v5`, `actions/deploy-pages@v5`.

---

## 🧪 Validar o repo antes da aula (checklist do instrutor)

Rode a lição localmente (Python puro, stdlib — nada a instalar):

```bash
cd cicd
python3 scripts/check.py     # deve imprimir APROVADO e sair 0
python3 scripts/build.py     # gera _site/index.html
open _site/index.html        # confira a renderização (1 e vários alunos)
```

Testes de borda esperados no `check.py` (todos devem **reprovar** com `exit 1` e
mensagem clara): nome com espaço/acento/maiúscula, arquivo vazio, arquivo sem
título, e pasta `alunos/` vazia.

Ensaio ponta a ponta num repo de teste (precisa do `gh` autenticado):

```bash
# 1) montar o repo standalone a partir de cicd/
mkdir /tmp/teste-aula-cicd && cp -R cicd/. /tmp/teste-aula-cicd/
cd /tmp/teste-aula-cicd && rm -rf _site
git init -b main && git add -A && git commit -m "pipeline inicial"

# 2) criar o repo e ligar o Pages com Source = GitHub Actions
gh repo create teste-aula-cicd --public --source=. --remote=origin
gh api -X POST repos/<SEU-USER>/teste-aula-cicd/pages -f build_type=workflow
git push -u origin main

# 3) acompanhar os 3 jobs
gh run watch <run-id> --exit-status

# 4) quebrar de propósito (apagar a linha "# ..." de alunos/exemplo.md),
#    commitar e confirmar: job 1 failure, jobs 2 e 3 skipped, site inalterado.
# 5) devolver o título, commitar e confirmar tudo verde de novo.
```

> Apagar o repo de teste no fim precisa do scope `delete_repo`:
> `gh auth refresh -h github.com -s delete_repo` e depois
> `gh repo delete <SEU-USER>/teste-aula-cicd --yes`.

---

## 🙅 O que NÃO dá para validar sem uma segunda conta

Alguns passos só existem na perspectiva de um **fork real** feito por outra conta:

- O botão **Fork** em si (passo 1).
- O banner **"I understand my workflows..."** (passo 2) — só aparece em repos
  forkados com Actions desabilitadas; nunca num repo criado por push.
- Permissões de Pages/`GITHUB_TOKEN` num fork.
- Concorrência de vários alunos commitando ao mesmo tempo (`concurrency: pages`).

---

**Material da aula "O que é DevOps & o conceito de CI/CD" — [ToolBox Technology](https://tbxtech.com.br/)** 🚀
