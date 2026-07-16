#!/usr/bin/env python3
"""Diagnostica por que o Render retorna 500 nas APIs"""
import urllib.request, json, subprocess, sys, os

BASE = "https://emotion-platform-albert.onrender.com"

def req(url, data=None, timeout=40):
    try:
        if data is not None:
            payload = json.dumps(data).encode() if isinstance(data, (dict, list)) else b""
            r = urllib.request.Request(url, data=payload, method="POST")
            r.add_header("Content-Type", "application/json")
        else:
            r = urllib.request.Request(url)
        with urllib.request.urlopen(r, timeout=timeout) as resp:
            body = resp.read().decode()
            return resp.status, body
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()[:200]
    except Exception as e:
        return 0, str(e)

print("=== DIAGNÓSTICO RENDER ===")

# Testar endpoints antigos (que funcionavam antes)
endpoints_antigos = [
    ("/api/v1/phq9/perguntas", None),
    ("/api/v1/gad7/perguntas", None),
    ("/api/v1/chat-ia/modelos/disponiveis", None),
    ("/api/v1/monitor/ping", None),
    ("/api/v1/stripe/planos", None),
    ("/api/v1/auth/stats/usuarios", None),
    ("/api/v1/multi-llm/modelos", None),
]

print("GET endpoints:")
for path, _ in endpoints_antigos:
    s, b = req(BASE + path)
    is_json = b.strip().startswith("{") or b.strip().startswith("[")
    if is_json:
        try:
            d = json.loads(b)
            print(f"  ✅ {path}: JSON OK")
        except:
            print(f"  ⚠️  {path}: {s} parse_error")
    else:
        print(f"  ❌ {path}: {s} HTML={b[:60]}")

# O problema: o health retorna HTML 500
# Significa que app está com erro de importação
print("\n=== IDENTIFICANDO O ERRO ===")
print("O Render retorna HTML de erro 500 — app crashou na inicialização")
print("Causa provável: import inválido no main.py ou plugin com erro")

# Testar localmente para encontrar o erro
result = subprocess.run(
    [sys.executable, "-c", """
import sys, traceback
sys.path.insert(0, '.')
try:
    from main import app
    print(f"OK: app carregou, rotas={len(app.routes)}")
except Exception as e:
    print(f"ERRO: {e}")
    traceback.print_exc()
"""],
    capture_output=True, text=True, timeout=60
)
print("\nTeste local:")
if result.stdout.strip():
    print(f"  {result.stdout.strip()}")
if result.returncode != 0:
    for line in result.stderr.splitlines()[-15:]:
        if line.strip():
            print(f"  {line}")
