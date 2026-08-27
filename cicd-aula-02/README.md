# Repositorio da turma — aula 2

Na aula 1 cada um tinha o proprio projeto. Aqui e diferente: **este projeto e de
todo mundo**, e nada entra nele sem passar pelo pipeline e por um colega.

Continua valendo: **ninguem instala nada.** Tudo pelo navegador.

## O fluxo de hoje

```
sua branch  →  Pull Request  →  pipeline confere  →  colega revisa  →  merge  →  publica
```

## Os passos

**1. Fork** deste repositorio (voce ja sabe: botao `Fork`).

**2. Crie sua branch.** No seu fork, no seletor de branch (escrito `main`),
digite um nome novo — `seunome-perfil` — e clique em *Create branch*.

**3. Faca sua mudanca** na sua branch: crie `alunos/seunome.md` com

```
# Seu Nome

Uma ou duas linhas sobre voce.
```

**4. Abra o Pull Request** para o repositorio da turma. O pipeline
`Conferir Pull Request` roda sozinho e mostra verde ou vermelho **antes** de
qualquer coisa entrar na `main`.

**5. Revise o PR de um colega.** Aba `Files changed` → `Review changes` →
comente e aprove (ou peca mudanca).

**6. Um mantenedor faz o merge.** So depois disso o site da turma e atualizado.

## Por que a `main` e protegida

Ninguem — nem voce, nem o professor — empurra direto na `main`. Todo mundo passa
por PR, pipeline e revisao. Nao e desconfianca: e o que impede que um erro de uma
pessoa quebre o trabalho de trinta.

## O manifesto (e o conflito)

`manifesto.md` tem uma linha por dupla. Os **dois** integrantes vao editar a
**mesma linha**, cada um no seu Pull Request.

O primeiro PR entra sem problema. O segundo vai mostrar:

> This branch has conflicts that must be resolved

Isso e um **conflito**. Nao e bug, nao e voce que errou: e o Git dizendo que duas
pessoas mudaram a mesma coisa e que ele nao vai escolher por voces. Resolvam
juntos, pelo proprio navegador, no botao `Resolve conflicts`.

Regra: nao apague o rotulo `N. Dupla N:`. Mude so o texto depois dos dois pontos.

## Os dois pipelines

| Arquivo | Quando roda | O que faz |
|---|---|---|
| `.github/workflows/pr.yml` | quando abre/atualiza um PR | so confere — nao publica |
| `.github/workflows/deploy.yml` | quando algo entra na `main` | confere, constroi e publica |

O segundo tem um detalhe: o passo de publicar espera **um humano aprovar**.
Isso tem nome — Continuous Delivery — e voces definiram na aula 1.

## Por que o pipeline do seu PR nao ve as senhas do projeto

Seu PR vem de um fork. O GitHub roda esse pipeline com permissao **somente
leitura** e **sem acesso aos segredos** do repositorio. Isso e de proposito: se
qualquer pessoa do mundo pudesse abrir um PR e o pipeline entregasse as senhas
do projeto pra ela, nao existiria projeto aberto na internet.
