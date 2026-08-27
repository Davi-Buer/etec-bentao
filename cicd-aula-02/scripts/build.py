"""
Transforma os arquivos .md da pasta alunos/ numa pagina HTML.

Sem biblioteca externa de proposito: e so Python puro lendo texto
e escrevendo HTML. Assim ninguem precisa instalar nada, nem aqui
nem no runner.
"""

import html
import pathlib
import re

TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Turma de CI/CD</title>
<style>
  :root { --navy:#012949; --azul:#0E5F9E; --amarelo:#FFD60A; --claro:#EDF3F8; }
  * { box-sizing:border-box; margin:0; padding:0; }
  body { font-family:system-ui,-apple-system,"Segoe UI",Arial,sans-serif;
         background:#fff; color:#12212E; line-height:1.6; }
  header { background:var(--navy); color:#fff; padding:56px 24px; }
  .wrap { max-width:880px; margin:0 auto; }
  header p.kicker { color:var(--amarelo); font-size:13px; font-weight:700;
                    letter-spacing:2px; text-transform:uppercase; }
  header h1 { font-size:42px; line-height:1.15; margin-top:10px; }
  header p.sub { color:#A9C6DE; margin-top:12px; font-size:17px; }
  main { padding:40px 24px 72px; }
  article { background:var(--claro); border-radius:12px; padding:24px 28px; margin-bottom:18px; }
  article h2 { color:var(--azul); font-size:24px; }
  .manifesto { border:2px solid var(--navy); border-radius:12px; padding:24px 28px; margin-bottom:28px; }
  .manifesto h2 { color:var(--navy); font-size:24px; }
  .manifesto ol { margin:12px 0 0 22px; }
  .manifesto li { margin-top:6px; }
  article p { margin-top:10px; }
  footer { border-top:1px solid #E1E7EC; padding:24px; text-align:center;
           color:#7A8894; font-size:13px; }
</style>
</head>
<body>
<header><div class="wrap">
  <p class="kicker">Publicado automaticamente por um pipeline</p>
  <h1>Turma de CI/CD</h1>
  <p class="sub">Esta pagina foi construida por um robo. Ninguem subiu arquivo na mao.</p>
</div></header>
<main><div class="wrap">
  <section class="manifesto">
    <h2>Manifesto da turma</h2>
    <ol>
{{MANIFESTO}}
    </ol>
  </section>
{{CARDS}}
</div></main>
<footer>{{TOTAL}} pessoa(s) nesta pagina &middot; gerado por scripts/build.py</footer>
</body>
</html>
"""


def montar_card(arquivo: pathlib.Path) -> str:
    linhas = [l.strip() for l in arquivo.read_text(encoding="utf-8").splitlines()]
    conteudo = [l for l in linhas if l]
    titulo = html.escape(conteudo[0].removeprefix("# ").strip())
    corpo = "\n".join(f"    <p>{html.escape(l)}</p>" for l in conteudo[1:])
    return f'  <article>\n    <h2>{titulo}</h2>\n{corpo}\n  </article>'


arquivos = sorted(pathlib.Path("alunos").glob("*.md"))
cards = "\n".join(montar_card(a) for a in arquivos)

itens = []
for linha in pathlib.Path("manifesto.md").read_text(encoding="utf-8").splitlines():
    linha = linha.strip()
    if re.match(r"^\d+\.", linha):
        texto = linha.split(":", 1)[1].strip() if ":" in linha else linha
        itens.append(f"      <li>{html.escape(texto)}</li>")
manifesto = "\n".join(itens)

pagina = (TEMPLATE
          .replace("{{CARDS}}", cards)
          .replace("{{MANIFESTO}}", manifesto)
          .replace("{{TOTAL}}", str(len(arquivos))))

saida = pathlib.Path("_site")
saida.mkdir(exist_ok=True)
(saida / "index.html").write_text(pagina, encoding="utf-8")

print(f"Site gerado com {len(arquivos)} arquivo(s).")
