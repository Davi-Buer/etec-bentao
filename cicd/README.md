# Aula de CI/CD — seu primeiro pipeline

Voce vai colocar um site no ar sem instalar nada no seu computador.
Tudo acontece no navegador.

## Os 5 passos

**1. Fork**
Botao `Fork` no canto superior direito desta pagina. Isso cria uma copia do
projeto dentro da sua conta.

**2. Ligar o robo**
Aba `Actions` → botao verde *"I understand my workflows, go ahead and enable them"*.

**3. Ligar a publicacao**
`Settings` → `Pages` → em **Source**, escolher **GitHub Actions**.

**4. Escrever seu arquivo**
Entre na pasta `cicd/alunos/` → `Add file` → `Create new file`.
Nome do arquivo: `seunome.md` (minusculo, sem espaco e sem acento).
Conteudo:

```
# Seu Nome

Escreva aqui uma ou duas linhas sobre voce.
```

Desca a pagina e clique no botao verde `Commit changes`.

**5. Ver o robo trabalhar**
Aba `Actions`. Voce vai ver os tres passos acontecendo em ordem:

```
1 - Verificar os arquivos  →  2 - Construir o site  →  3 - Publicar na internet
```

Quando ficar tudo verde, volte em `Settings` → `Pages` e clique no link.
Esse endereco e publico.

## As regras do projeto

O passo 1 do pipeline (`cicd/scripts/check.py`) confere tres coisas:

1. O nome do arquivo tem so letras minusculas, numeros, hifen e ponto.
2. A primeira linha comeca com `# ` (o titulo).
3. Existe pelo menos uma linha alem do titulo.

Se qualquer uma falhar, o pipeline fica **vermelho**, os passos 2 e 3 nao rodam
e o site **nao e atualizado**. O que ja estava no ar continua no ar.

Isso e integracao continua: o erro para antes de chegar em alguem.

## Exercicio: quebre de proposito

Abra o seu arquivo em `cicd/alunos/`, **apague a linha do titulo** (a que comeca com `# `)
e faca commit.

Va na aba `Actions`. O passo 1 fica vermelho e os passos 2 e 3 ficam cinzas —
eles nem chegaram a rodar. Agora abra o seu site: ele continua no ar, com o
conteudo antigo.

Depois devolva o titulo, faca commit e espere o verde voltar.

## Quando alguma coisa da errado

| O que voce ve | O que fazer |
|---|---|
| A aba Actions esta vazia | Voce pulou o passo 2. Ligue os workflows. |
| Passo 3 falha com erro de Pages | Voce pulou o passo 3. Source tem que ser **GitHub Actions**, nao "Deploy from a branch". |
| Passo 1 vermelho | Leia a mensagem — ela diz exatamente qual regra voce quebrou. |
| O site abre em branco | Espere 1 minuto e recarregue com Ctrl+F5. A primeira publicacao demora um pouco. |
| Nada acontece depois do commit | Confira se voce commitou na branch `main`. |

## O que voce leva daqui

Este repositorio e publico e fica com voce. Ele mostra, de forma verificavel,
que voce configurou um pipeline de CI/CD e colocou um site em producao.
Isso vale mais num processo seletivo do que qualquer linha de curriculo.

---
Material da aula "O que e DevOps & o conceito de CI/CD" — TBX Tech
