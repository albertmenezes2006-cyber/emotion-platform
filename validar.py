#!/usr/bin/env python3
"""
Emotion Intelligence Platform — Validador Automático
Roda: python3 validar.py
"""
import py_compile
import os
import sys
import subprocess
from datetime import datetime

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    console = Console()
    USE_RICH = True
except ImportError:
    USE_RICH = False

MAIN = "main.py"
TEMPLATES_DIR = "templates"

FUNCOES_ESPERADAS = [
    "verificar_token",
    "analisar_emocao",
    "obter_perfil_sofia",
    "detectar_idioma",
]

ENDPOINTS_ESPERADOS = [
    '@app.get("/")',
    '@app.post("/api/v1/analisar")',
    '@app.get("/dashboard")',
    '@app.get("/chat")',
    '@app.get("/health")',
]

BLOCOS_ESPERADOS = {
    "Bloco 1": "BLOCO 1/32500",
    "Bloco 2": "BLOCO 2/32500",
    "Bloco 3": "BLOCO 3/32500",
}

resultados = []
erros = []
avisos = []

def ok(msg):
    resultados.append(("✅", msg))

def erro(msg):
    resultados.append(("❌", msg))
    erros.append(msg)

def aviso(msg):
    resultados.append(("⚠️ ", msg))
    avisos.append(msg)

# ── Verificações
print("")

# 1. Arquivo existe
if os.path.exists(MAIN):
    ok(f"{MAIN} encontrado")
else:
    erro(f"{MAIN} NÃO encontrado")
    sys.exit(1)

with open(MAIN, "r", encoding="utf-8") as f:
    content = f.read()
    lines = content.split("\n")
    total_lines = len(lines)

# 2. Sintaxe
try:
    py_compile.compile(MAIN, doraise=True)
    ok(f"Sintaxe Python OK")
except py_compile.PyCompileError as e:
    erro(f"ERRO de sintaxe: {e}")

# 3. Contagem de linhas
ok(f"Total de linhas: {total_lines:,}")
if total_lines < 1000:
    aviso("main.py muito pequeno — possível corrupção")

# 4. Templates
if os.path.isdir(TEMPLATES_DIR):
    templates = [f for f in os.listdir(TEMPLATES_DIR) if f.endswith(".html")]
    ok(f"Templates: {len(templates)} HTML encontrados")
else:
    erro("Pasta templates/ não encontrada")

# 5. Funções esperadas
for func in FUNCOES_ESPERADAS:
    if f"def {func}" in content or f"async def {func}" in content:
        ok(f"Função {func}() OK")
    else:
        aviso(f"Função {func}() não encontrada")

# 6. Endpoints esperados
for ep in ENDPOINTS_ESPERADOS:
    if ep in content:
        ok(f"Endpoint {ep} OK")
    else:
        aviso(f"Endpoint {ep} não encontrado")

# 7. Blocos implementados
for nome, marker in BLOCOS_ESPERADOS.items():
    if marker in content:
        ok(f"{nome}: IMPLEMENTADO")
    else:
        aviso(f"{nome}: não encontrado ainda")

# 8. Duplicatas perigosas
funcoes_criticas = ["def analisar_emocao", "def verificar_token", "def obter_perfil_sofia"]
for func in funcoes_criticas:
    count = content.count(func)
    if count > 1:
        erro(f"DUPLICATA: {func} aparece {count}x")
    elif count == 1:
        ok(f"Sem duplicata: {func}")

# 9. Imports críticos
imports_criticos = ["fastapi", "asyncpg", "uvicorn"]
for imp in imports_criticos:
    if imp in content.lower():
        ok(f"Import {imp} presente")
    else:
        aviso(f"Import {imp} não encontrado")

# 10. Backup existe
if os.path.exists("main.py.bak"):
    ok("Backup main.py.bak existe")
else:
    aviso("Sem backup — rode: cp main.py main.py.bak")

# 11. Git status
try:
    result = subprocess.run(["git", "status", "--short"], capture_output=True, text=True)
    mudancas = result.stdout.strip()
    if mudancas:
        ok(f"Git: {len(mudancas.split(chr(10)))} arquivo(s) modificado(s)")
    else:
        ok("Git: tudo commitado")
except Exception:
    aviso("Git não disponível")

# 12. Requirements
if os.path.exists("requirements.txt"):
    with open("requirements.txt") as f:
        reqs = f.read()
    ok(f"requirements.txt presente")
else:
    aviso("requirements.txt não encontrado")

# ── Output
print("═" * 50)
print("  EMOTION PLATFORM — VALIDADOR v1.0")
print(f"  {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
print("═" * 50)

for icone, msg in resultados:
    print(f"  {icone} {msg}")

print("─" * 50)
print(f"  Total: {len(resultados)} verificações")
print(f"  Erros: {len(erros)} | Avisos: {len(avisos)}")
print("─" * 50)

if erros:
    print("  ❌ RESULTADO: CORRIJA OS ERROS — não faça push!")
    for e in erros:
        print(f"     → {e}")
    sys.exit(1)
elif avisos:
    print("  ⚠️  RESULTADO: OK com avisos — push com cuidado")
    sys.exit(0)
else:
    print("  ✅ RESULTADO: TUDO PERFEITO — pode fazer push!")
    sys.exit(0)

print("═" * 50)
print("")
