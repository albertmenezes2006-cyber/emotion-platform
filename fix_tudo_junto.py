#!/usr/bin/env python3
"""FIX TUDO — GitHub workflow + teste direto + diagnóstico"""
import os, subprocess, sys, urllib.request, json

def w(path, content):
    os.makedirs(os.path.dirname(path) if os.path.dirname(path) else ".", exist_ok=True)
    with open(path, "w") as f:
        f.write(content)
    print(f"✅ {path}")

# ══════════════════════════════════════════════
# 1. REMOVER workflow (precisa de permissão especial)
# ══════════════════════════════════════════════
if os.path.exists(".github/workflows/keepalive.yml"):
    os.remove(".github/workflows/keepalive.yml")
    print("✅ keepalive.yml removido (precisa de token com workflow scope)")

# ══════════════════════════════════════════════
# 2. CRIAR SCRIPT DE KEEP-ALIVE LOCAL
# ══════════════════════════════════════════════
w("keepalive_render.sh", """#!/bin/bash
# Mantém o Render acordado — rode em background
# Usage: bash keepalive_render.sh &
URL="https://emotion-platform-albert.onrender.com/health"
while true; do
    echo "[$(date +%H:%M)] Ping..."
    curl -s --max-time 30 "$URL" > /dev/null && echo "OK" || echo "FALHOU"
    sleep 840  # 14 minutos
done
""")

# ══════════════════════════════════════════════
# 3. DIAGNÓSTICO DO PROBLEMA DOS POSTS
# ══════════════════════════════════════════════
print("\n=== DIAGNÓSTICO ===")
BASE = "https://emotion-platform-albert.onrender.com"

# Testar GET primeiro
try:
    with urllib.request.urlopen(BASE + "/health", timeout=30) as r:
        data = json.loads(r.read())
        print(f"✅ GET /health: {data}")
except Exception as e:
    print(f"❌ GET /health: {e}")

# Testar POST com urllib (sem curl)
try:
    import urllib.parse
    dados = urllib.parse.urlencode({}).encode()
    url = BASE + "/api/v1/auth/cadastrar?nome=Teste&email=fix@test.com&senha=Fix12345&tipo=paciente"
    req = urllib.request.Request(url, data=dados, method="POST")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    with urllib.request.urlopen(req, timeout=40) as r:
        data = json.loads(r.read())
        print(f"✅ POST /auth/cadastrar: user_id={data.get('user_id')} status={data.get('status')}")
        print(f"   Token: {data.get('token','')[:50]}...")
except Exception as e:
    print(f"❌ POST /auth/cadastrar: {e}")

# Testar chat IA
try:
    payload = json.dumps({
        "user_id": "fix_test",
        "mensagem": "Ola, estou me sentindo bem hoje"
    }).encode()
    req = urllib.request.Request(
        BASE + "/api/v1/chat-ia/mensagem",
        data=payload,
        method="POST"
    )
    req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=45) as r:
        data = json.loads(r.read())
        print(f"✅ POST /chat-ia: modelo={data.get('modelo_usado')}")
        print(f"   Resposta: {str(data.get('resposta',''))[:100]}...")
except Exception as e:
    print(f"❌ POST /chat-ia: {e}")

# Testar multi-llm
try:
    url = BASE + "/api/v1/multi-llm/chat?mensagem=Ola&user_id=test"
    req = urllib.request.Request(url, data=b"", method="POST")
    with urllib.request.urlopen(req, timeout=45) as r:
        data = json.loads(r.read())
        print(f"✅ POST /multi-llm: modelo={data.get('modelo_usado')}")
        print(f"   Resposta: {str(data.get('resposta',''))[:100]}...")
except Exception as e:
    print(f"❌ POST /multi-llm/chat: {e}")

# ══════════════════════════════════════════════
# 4. TESTAR LOCALMENTE (sem Render)
# ══════════════════════════════════════════════
print("\n=== TESTE LOCAL (sem depender do Render) ===")
result = subprocess.run(
    [sys.executable, "-c", """
import sys; sys.path.insert(0,'.')
from main import app
from fastapi.testclient import TestClient
c = TestClient(app, raise_server_exceptions=False)

testes = [
    ("GET",  "/health",                        None, "Health"),
    ("GET",  "/api/v1/stripe/planos",          None, "Planos Stripe"),
    ("GET",  "/api/v1/auth/stats/usuarios",    None, "Auth Stats"),
    ("GET",  "/api/v1/multi-llm/modelos",      None, "Multi-LLM Modelos"),
    ("GET",  "/api/mobile/v1/sdk/config",      None, "Mobile SDK"),
    ("GET",  "/api/v1/phq9/perguntas",         None, "PHQ-9 Perguntas"),
    ("GET",  "/api/v1/monitor/status-completo",None, "Monitor"),
    ("POST", "/api/v1/auth/cadastrar?nome=Albert&email=local@test.com&senha=Test1234&tipo=paciente", None, "Auth Cadastro"),
    ("POST", "/api/v1/chat-ia/mensagem",       {"user_id":"test","mensagem":"Ola"}, "Chat IA"),
    ("POST", "/api/v1/multi-llm/chat?mensagem=Ola&user_id=test", None, "Multi-LLM Chat"),
    ("GET",  "/app/avaliacao",                 None, "Pagina Avaliacao"),
    ("GET",  "/app/chat",                      None, "Pagina Chat"),
    ("GET",  "/app/planos",                    None, "Pagina Planos"),
    ("GET",  "/app/login",                     None, "Pagina Login"),
    ("GET",  "/docs",                          None, "API Docs"),
]

ok = err = 0
for method, path, body, nome in testes:
    try:
        if method == "POST":
            r = c.post(path, json=body) if body else c.post(path)
        else:
            r = c.get(path)
        s = "OK" if r.status_code < 400 else "ERRO"
        ic = "OK" if r.status_code < 400 else "XX"
        print(f"  [{ic}] {nome}: {r.status_code}")
        if r.status_code < 400: ok += 1
        else: err += 1
    except Exception as e:
        print(f"  [EX] {nome}: {str(e)[:60]}")
        err += 1

print(f"  Resultado: {ok}/{len(testes)} OK | {err} erros")
print(f"  Rotas: {len(app.routes)}")

# Testar auth completo
print("  --- AUTH FLOW ---")
try:
    r = c.post("/api/v1/auth/cadastrar?nome=AlbertM&email=am@test.com&senha=Senha123&tipo=terapeuta")
    if r.status_code == 200:
        d = r.json()
        tok = d.get("token","")
        print(f"  Cadastro: {d.get('status')} | user={d.get('user_id')}")
        print(f"  Token: {tok[:60]}...")
        r2 = c.get("/api/v1/auth/me", headers={"Authorization": f"Bearer {tok}"})
        print(f"  /me: {r2.status_code} | {r2.json()}")
    else:
        print(f"  Cadastro: {r.status_code} {r.text[:100]}")
except Exception as e:
    print(f"  Auth erro: {e}")

# Testar chat local
print("  --- CHAT IA LOCAL ---")
try:
    r = c.post("/api/v1/chat-ia/mensagem", json={"user_id":"albert","mensagem":"Estou ansioso"})
    if r.status_code == 200:
        d = r.json()
        print(f"  Chat: modelo={d.get('modelo_usado')}")
        print(f"  Resp: {str(d.get('resposta',''))[:100]}...")
    else:
        print(f"  Chat: {r.status_code}")
except Exception as e:
    print(f"  Chat erro: {e}")
"""],
    capture_output=True, text=True, timeout=120
)
# Mostrar apenas linhas relevantes
for line in result.stdout.splitlines():
    if line.strip():
        print(line)
if result.returncode != 0:
    erros = [l for l in result.stderr.splitlines() if "ERROR" in l or "Error" in l][:5]
    for e in erros:
        print(f"  ⚠️ {e}")

# ══════════════════════════════════════════════
# 5. COMMIT E PUSH (sem workflow)
# ══════════════════════════════════════════════
print("\n=== GIT PUSH ===")
cmds = [
    ["git", "add", "-A"],
    ["git", "commit", "-m", "fix: remove workflow (precisa permissao) + keepalive.sh + diagnostico completo"],
    ["git", "push"],
]
for cmd in cmds:
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode == 0:
        print(f"✅ {' '.join(cmd[:2])}")
    else:
        print(f"❌ {' '.join(cmd[:2])}: {r.stderr[:100]}")

print("\n" + "="*55)
print("RESUMO FINAL")
print("="*55)
print("  Site: https://emotion-platform-albert.onrender.com")
print("  Docs: https://emotion-platform-albert.onrender.com/docs")
print("  Avaliação: /app/avaliacao")
print("  Chat: /app/chat")
print("  Login: /app/login")
print("  Planos: /app/planos")
print("="*55)
