# 🚦 Roteiro da aula — O que é DevOps & o conceito de CI/CD

Roteiro do **instrutor** para a aula de CI/CD. Os alunos usam **só o navegador**
(nada instalado): forkam este repositório → editam um `.md` pela web → veem a
Action rodar → abrem a página no ar. O material da lição fica em [`cicd/`](cicd/).

> A página que o aluno lê durante a aula é o [`cicd/README.md`](cicd/README.md).
> Este roteiro é o guia de bastidores: critérios de aceite + como validar o repo
> antes da turma.

---

## 🎯 O que o aluno faz (os 5 passos)

Descritos em detalhe no [`cicd/README.md`](cicd/README.md):

1. **Fork** deste repositório (o `etec-bentao` inteiro) para a conta dele.
2. **Ligar o robô** — aba `Actions` → "I understand my workflows, go ahead and enable them".
3. **Ligar a publicação** — `Settings` → `Pages` → **Source = GitHub Actions**.
4. **Escrever o arquivo** — `cicd/alunos/seunome.md` (minúsculo, sem espaço, sem acento).
5. **Ver o robô trabalhar** — 3 jobs em ordem, depois abrir o link do Pages.

Depois: **quebrar de propósito** (apagar a linha do título de `cicd/alunos/...`),
ver o pipeline ficar vermelho e o site **não** mudar, e então consertar e voltar
ao verde.

---

## ✅ Critérios de aceite (o que o pipeline garante)

O job 1 (`cicd/scripts/check.py`) reprova o commit — **e o site não é publicado** —
se qualquer uma destas regras falhar:

1. **Nome do arquivo** só com `a-z`, `0-9`, `.`, `-` (sem espaço, sem acento, sem
   maiúscula). Regex: `[a-z0-9._-]+`.
2. **Primeira linha é o título**, começando com `# `.
3. **Há pelo menos uma linha** além do título.
4. A pasta `cicd/alunos/` **não pode estar vazia**.

Comportamento esperado do pipeline (é o coração da aula):

| Situação | Job 1 Verificar | Job 2 Construir | Job 3 Publicar | Site no ar |
|---|---|---|---|---|
| Arquivo válido | ✅ success | ✅ success | ✅ success | atualizado |
| Regra quebrada | ❌ **failure** | ⚪ **skipped** | ⚪ **skipped** | **inalterado** |

Os jobs 2 e 3 ficam **skipped** (cinza), **não** failed, porque encadeiam com
`needs:` (`construir needs verificar`, `publicar needs construir`). O deploy nem
roda → a versão que já estava em produção continua intacta. **Isso é integração
contínua: o erro para antes de chegar em alguém.**

Garantias de segurança do `cicd/scripts/build.py`: título e corpo passam por
`html.escape()`, então `<` e `&` viram texto literal — sem quebrar o HTML e sem
permitir injeção.

---

## 🗂️ Layout (importante)

O aluno forka o **monorepo inteiro**, e o GitHub só executa workflows que estão em
`.github/workflows/` na **raiz** do repositório. Por isso o workflow fica em
[`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) (na raiz), mas a
lição vive em `cicd/`. A ponte entre os dois é:

- `defaults.run.working-directory: cicd` → os comandos `python3 scripts/check.py`
  e `python3 scripts/build.py` rodam de dentro de `cicd/` (onde estão `scripts/` e
  `alunos/`).
- `upload-pages-artifact` usa `path: cicd/_site` (esse caminho é relativo à raiz
  do repositório, não ao `working-directory`).

> ⚠️ O workflow **precisa** ficar na raiz. Um `deploy.yml` dentro de
> `cicd/.github/` **não roda** num fork do monorepo — o GitHub ignora workflows
> fora da raiz.

Versões das actions (mantidas em tags de major, legíveis para os alunos):
`actions/checkout@v7`, `actions/upload-pages-artifact@v5`, `actions/deploy-pages@v5`.

> Observação: como o workflow dispara em `push` na `main`, o próprio `etec-bentao`
> também publica um Pages (a turma com o `exemplo.md`). Se não quiser isso no repo
> de origem, é só não habilitar Pages nele — os forks dos alunos habilitam o
> deles normalmente.

---

## 🧪 Validar o repo antes da aula (checklist do instrutor)

Rode a lição localmente (Python puro, stdlib — nada a instalar):

```bash
cd cicd
python3 scripts/check.py     # deve imprimir APROVADO e sair 0
python3 scripts/build.py     # gera cicd/_site/index.html
open _site/index.html        # confira a renderização (1 e vários alunos)
```

Testes de borda esperados no `check.py` (todos devem **reprovar** com `exit 1` e
mensagem clara): nome com espaço/acento/maiúscula, arquivo vazio, arquivo sem
título, e pasta `alunos/` vazia.

Ensaio ponta a ponta (precisa do `gh` autenticado). Como o aluno forka o monorepo,
o teste é feito com este repositório inteiro:

```bash
# 1) empurrar este repo para um repositorio de teste
gh repo create teste-aula-cicd --public --source=. --remote=teste --push

# 2) ligar o Pages com Source = GitHub Actions
gh api -X POST repos/<SEU-USER>/teste-aula-cicd/pages -f build_type=workflow

# 3) acompanhar os 3 jobs (o run dispara no push)
gh run watch <run-id> --exit-status

# 4) quebrar de proposito: apagar a linha "# ..." de cicd/alunos/exemplo.md,
#    commitar e confirmar: job 1 failure, jobs 2 e 3 skipped, site inalterado.
# 5) devolver o titulo, commitar e confirmar tudo verde de novo.
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
