# Checklist do instrutor — antes da aula 2

Nao pule nenhum. Os dois primeiros travam a sala inteira.

## 1. Liberar workflow de PR vindo de fork  [BLOCKER]
`Settings → Actions → General → Fork pull request workflows`.
Por padrao, PR de quem nunca contribuiu **exige sua aprovacao manual** antes do
workflow rodar. Com 30 alunos, sao 30 cliques seus com a turma parada.
**Teste com uma conta que NUNCA contribuiu aqui.** Testar com a sua da falso positivo.

## 2. Concorrencia do deploy  [BLOCKER]
Ja esta como `cancel-in-progress: true` no `deploy.yml`. Nao mudar: 30 merges
seguidos com `false` viram 30 publicacoes na fila.

## 3. Repositorio PUBLICO
Required reviewers em Environments so e gratuito em repo publico
(Free/Pro/Team). Em privado exige Enterprise. Sem isso, a Recompensa 3 nao existe.

## 4. Environment `producao`
`Settings → Environments → New environment` → nome `producao` →
marcar **Required reviewers** → adicionar voce (e 1 aluno mantenedor, se quiser).

## 5. Branch protection na `main`
`Settings → Rules / Branches`: exigir PR, exigir 1 aprovacao, exigir o check
`Verificar os arquivos` do workflow de PR.

## 6. Pages
`Settings → Pages → Source = GitHub Actions`.

## 7. Mantenedores
Adicionar 3–4 alunos como colaboradores com permissao de merge.
Escolher os que mexeram no `deploy.yml` sozinhos depois da aula 1.
Vira cargo — adolescente responde bem a cargo.

## 8. Ajustar o manifesto
`manifesto.md` vem com 15 duplas. Corte para o numero real de duplas da turma.

## 9. Ensaio geral
Com uma segunda conta: fork → branch → PR → ver o pipeline rodar → merge →
ver a aprovacao de deploy pendente → aprovar → site atualizado.
Se esse ensaio nao rodar inteiro, a aula nao esta pronta.
