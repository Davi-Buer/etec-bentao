"""
As regras do projeto.

Se qualquer regra for quebrada, este script termina com erro,
o pipeline fica VERMELHO e o site NAO e publicado.
O site que ja estava no ar continua no ar, com o conteudo antigo.

Isso e integracao continua: o erro para aqui, antes de chegar em alguem.
"""

import pathlib
import re
import sys

ERROS = []
PASTA = pathlib.Path("alunos")

arquivos = sorted(PASTA.glob("*.md"))

if not arquivos:
    ERROS.append("A pasta alunos/ esta vazia — crie o seu arquivo .md")

for arquivo in arquivos:
    # Regra 1 — nome do arquivo sem espaco, sem acento, tudo minusculo
    if not re.fullmatch(r"[a-z0-9._-]+", arquivo.name):
        ERROS.append(
            f"{arquivo.name}: use so letras minusculas, numeros, hifen e ponto "
            f"(sem espaco e sem acento)."
        )

    linhas = [l.strip() for l in arquivo.read_text(encoding="utf-8").splitlines()]
    conteudo = [l for l in linhas if l]

    # Regra 2 — a primeira linha precisa ser o titulo
    tem_titulo = bool(conteudo) and conteudo[0].startswith("# ")
    if not tem_titulo:
        ERROS.append(
            f"{arquivo.name}: a primeira linha precisa ser o titulo, comecando com '# '."
        )

    # Regra 3 — precisa ter conteudo alem do titulo
    elif len(conteudo) < 2:
        ERROS.append(f"{arquivo.name}: escreva pelo menos uma linha alem do titulo.")

# Regra 4 — o manifesto da turma precisa manter a estrutura
manifesto = pathlib.Path("manifesto.md")
if not manifesto.exists():
    ERROS.append("manifesto.md sumiu — ele nao pode ser apagado.")
else:
    linhas = manifesto.read_text(encoding="utf-8").splitlines()
    numeradas = [l for l in linhas if re.match(r"^\d+\.", l.strip())]
    if not numeradas:
        ERROS.append("manifesto.md: nenhuma linha numerada sobrou.")
    for linha in numeradas:
        if not re.match(r"^(\d+)\. Dupla \1:", linha.strip()):
            ERROS.append(
                f'manifesto.md: a linha "{linha.strip()[:40]}" perdeu o rotulo. '
                f'Mude so o texto DEPOIS dos dois pontos.'
            )

if ERROS:
    print("REPROVADO — o site NAO vai ser publicado.\n")
    for erro in ERROS:
        print("  [x] " + erro)
    print("\nConserte o erro acima, faca um novo commit e o robo tenta de novo.")
    sys.exit(1)

print(f"APROVADO — {len(arquivos)} arquivo(s) em ordem. Pode publicar.")
