#!/usr/bin/env python3
import py_compile, os, sys, subprocess
from datetime import datetime

MAIN = "main.py"
resultados = []
erros = []
avisos = []

def ok(m): resultados.append(("✅", m))
def erro(m): resultados.append(("❌", m)); erros.append(m)
def av(m): resultados.append(("⚠️ ", m)); avisos.append(m)

if not os.path.exists(MAIN): erro("main.py não encontrado"); sys.exit(1)

with open(MAIN, "r") as f:
    content = f.read()
    total = len(content.split("\n"))

# Sintaxe
try:
    py_compile.compile(MAIN, doraise=True); ok("Sintaxe OK")
except py_compile.PyCompileError as e:
    erro(f"Sintaxe ERRO: {e}")

ok(f"Linhas: {total:,}")
if total < 1000: av("main.py muito pequeno")

# Templates
if os.path.isdir("templates"):
    t = [f for f in os.listdir("templates") if f.endswith(".html")]
    ok(f"Templates: {len(t)} HTML")
else: erro("templates/ não encontrada")

# Funções — nomes reais do projeto
for fn in ["verificar_token","obter_perfil_sofia","detectar_idioma","detectar_emocao"]:
    if f"def {fn}" in content or f"async def {fn}" in content: ok(f"{fn}() OK")
    else: av(f"{fn}() não encontrada")

# Endpoints — formato real do projeto
for ep in [
    ('"/"',          "/"),
    ('"/dashboard"',  "/dashboard"),
    ('"/chat"',       "/chat"),
    ('"/health"',     "/health"),
    ('"/terapia"',    "/terapia"),
    ('"/ranking"',    "/ranking"),
    ('"/blog"',       "/blog"),
    ('"/api/v1/analisar"', "/api/v1/analisar"),
]:
    if ep[0] in content: ok(f"{ep[1]} OK")
    else: av(f"{ep[1]} não encontrado")

# Blocos implementados
for b, m in [("4","BLOCO 4/32500"),("5","BLOCO 5/32500"),("6","BLOCO 6/32500")]:
    if m in content: ok(f"Bloco {b}: IMPLEMENTADO")
    else: av(f"Bloco {b}: pendente")

# Duplicatas
for fn in ["def detectar_emocao(","def verificar_token","def obter_perfil_sofia"]:
    c = content.count(fn)
    if c > 1: erro(f"DUPLICATA: {fn} aparece {c}x")
    elif c == 1: ok(f"Sem duplicata: {fn}")

# Imports reais
for imp in ["fastapi","uvicorn","sqlalchemy"]:
    if imp in content.lower(): ok(f"Import {imp} OK")
    else: av(f"Import {imp} não encontrado")

# Backup
if os.path.exists("main.py.bak"): ok("Backup OK")
else: av("Sem backup")

# Git
try:
    r = subprocess.run(["git","status","--short"], capture_output=True, text=True)
    m = r.stdout.strip()
    if m: ok(f"Git: {len(m.split(chr(10)))} modificado(s)")
    else: ok("Git: tudo commitado")
except: av("Git indisponível")

# Requirements
if os.path.exists("requirements.txt"): ok("requirements.txt OK")
else: av("requirements.txt não encontrado")

# Output
print("\n" + "═"*50)
print("  EMOTION PLATFORM — VALIDADOR v2.0")
print(f"  {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
print("═"*50)
for i, m in resultados: print(f"  {i} {m}")
print("─"*50)
print(f"  Total: {len(resultados)} | Erros: {len(erros)} | Avisos: {len(avisos)}")
print("─"*50)
if erros:
    print("  ❌ CORRIJA OS ERROS — não faça push!")
    for e in erros: print(f"     → {e}")
    sys.exit(1)
elif avisos:
    print("  ⚠️  OK com avisos — push com cuidado")
else:
    print("  ✅ TUDO PERFEITO — pode fazer push!")
print("═"*50 + "\n")
