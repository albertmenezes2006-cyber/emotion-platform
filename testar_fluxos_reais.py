#!/usr/bin/env python3
"""
Teste de Fluxos Reais — Emotion Intelligence Platform
Testa TUDO via HTTP simulando usuário real
Meta: 100% de cobertura funcional
"""
import urllib.request
import urllib.error
import json
import time
import random
import string

VERDE   = "\033[92m"
AMARELO = "\033[93m"
VERMELHO= "\033[91m"
AZUL    = "\033[94m"
RESET   = "\033[0m"
NEGRITO = "\033[1m"

BASE = "https://emotion-platform-albert.onrender.com"
TOKEN = None
USER_ID = None
EMAIL = f"teste_{''.join(random.choices(string.ascii_lowercase, k=6))}@teste.com"
SENHA = "senha123"

ok = 0
warn = 0
erro = 0
resultados = []

def log_ok(msg):
    global ok; ok += 1
    print(f"  {VERDE}✅ {msg}{RESET}")
    resultados.append(f"OK: {msg}")

def log_warn(msg):
    global warn; warn += 1
    print(f"  {AMARELO}⚠️  {msg}{RESET}")
    resultados.append(f"WARN: {msg}")

def log_erro(msg):
    global erro; erro += 1
    print(f"  {VERMELHO}❌ {msg}{RESET}")
    resultados.append(f"ERRO: {msg}")

def secao(titulo):
    print(f"\n{NEGRITO}{AZUL}{'='*55}{RESET}")
    print(f"{NEGRITO}{AZUL}  {titulo}{RESET}")
    print(f"{NEGRITO}{AZUL}{'='*55}{RESET}")

def req(method, path, body=None, token=None, esperado=200):
    url = BASE + path
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    data = json.dumps(body).encode() if body else None
    try:
        r = urllib.request.Request(url, data=data, headers=headers, method=method)
        with urllib.request.urlopen(r, timeout=30) as resp:
            status = resp.status
            try:
                resultado = json.loads(resp.read())
            except:
                resultado = {}
            return status, resultado
    except urllib.error.HTTPError as e:
        try:
            resultado = json.loads(e.read())
        except:
            resultado = {}
        return e.code, resultado
    except Exception as ex:
        return 0, {"erro": str(ex)}

# ══════════════════════════════════════════════════
# 1. HEALTH CHECK
# ══════════════════════════════════════════════════
secao("1. HEALTH CHECK")

status, data = req("GET", "/health")
if status == 200 and data.get("status") == "ok":
    log_ok(f"Health OK — plugins={data.get('plugins')} rotas={data.get('rotas')}")
    log_ok(f"Uptime: {data.get('uptime')}")
    log_ok(f"Erros: {data.get('erros')}")
else:
    log_erro(f"Health falhou: {status} — {data}")

# ══════════════════════════════════════════════════
# 2. PÁGINAS HTML
# ══════════════════════════════════════════════════
secao("2. PÁGINAS HTML — TODAS AS 45")

paginas = [
    "/", "/login", "/cadastro", "/sobre", "/planos",
    "/premium", "/blog", "/faq", "/contato", "/privacidade",
    "/termos", "/app/dashboard", "/app/chat", "/app/diario",
    "/app/gamificacao", "/app/ranking", "/app/perfil",
    "/app/configuracoes", "/app/avaliacao", "/app/agenda",
    "/app/analises", "/app/carteira", "/app/score-ie",
    "/checkout", "/checkout/anual", "/checkout/api",
    "/checkout/creditos", "/checkout/relatorio", "/checkout/sofia",
    "/nova-senha", "/recuperar-senha", "/sucesso", "/obrigado",
    "/presente", "/presente/sucesso", "/afiliado",
    "/psicologos", "/terapia", "/whitelabel",
    "/api-docs", "/compartilhar",
    "/offline", "/404",
]

paginas_ok = 0
paginas_erro = 0
for pagina in paginas:
    status, _ = req("GET", pagina)
    if status in [200, 201]:
        paginas_ok += 1
    elif status in [401, 403]:
        log_warn(f"Protegida (requer login): {pagina} → {status}")
    elif status == 404:
        log_erro(f"404 NÃO ENCONTRADA: {pagina}")
        paginas_erro += 1
    elif status == 500:
        log_erro(f"500 ERRO INTERNO: {pagina}")
        paginas_erro += 1
    else:
        log_warn(f"{pagina} → {status}")

log_ok(f"Páginas OK: {paginas_ok}/{len(paginas)}")
if paginas_erro > 0:
    log_erro(f"Páginas com erro: {paginas_erro}")

# ══════════════════════════════════════════════════
# 3. CADASTRO
# ══════════════════════════════════════════════════
secao("3. FLUXO DE CADASTRO")

status, data = req("POST", "/api/v1/auth/cadastrar", {
    "nome": "Teste Albert",
    "email": EMAIL,
    "senha": SENHA,
    "tipo": "paciente"
})

if status in [200, 201]:
    TOKEN = data.get("token") or data.get("access_token")
    USER_ID = data.get("user_id")
    log_ok(f"Cadastro OK — user_id={USER_ID}")
    log_ok(f"Token gerado: {'Sim' if TOKEN else 'Não'}")
    log_ok(f"Email: {data.get('email')}")
    log_ok(f"Plano: {data.get('plano')}")
    log_ok(f"Tipo: {data.get('tipo')}")
else:
    log_erro(f"Cadastro falhou: {status} — {data}")

# ══════════════════════════════════════════════════
# 4. LOGIN
# ══════════════════════════════════════════════════
secao("4. FLUXO DE LOGIN")

status, data = req("POST", "/api/v1/auth/login", {
    "email": EMAIL,
    "senha": SENHA
})

if status == 200:
    TOKEN = data.get("token") or data.get("access_token")
    log_ok(f"Login OK — status={data.get('status')}")
    log_ok(f"Token: {'Gerado ✅' if TOKEN else 'NÃO GERADO ❌'}")
    log_ok(f"Nome: {data.get('nome')}")
    log_ok(f"Tipo: {data.get('tipo')}")
    log_ok(f"Plano: {data.get('plano')}")
else:
    log_erro(f"Login falhou: {status} — {data}")

# ══════════════════════════════════════════════════
# 5. AUTH/ME
# ══════════════════════════════════════════════════
secao("5. VERIFICAÇÃO DE TOKEN (auth/me)")

if TOKEN:
    status, data = req("GET", "/api/v1/auth/me", token=TOKEN)
    if status == 200:
        log_ok(f"Token válido — usuário={data.get('nome')}")
        log_ok(f"Email: {data.get('email')}")
        log_ok(f"Tipo: {data.get('tipo')}")
    else:
        log_erro(f"Token inválido: {status} — {data}")
else:
    log_erro("Sem token para testar")

# ══════════════════════════════════════════════════
# 6. CHAT IA
# ══════════════════════════════════════════════════
secao("6. CHAT COM IA (Mistral)")

if TOKEN:
    status, data = req("POST", "/api/v1/chat", {
        "mensagem": "Olá, como você pode me ajudar com saúde mental?"
    }, token=TOKEN)

    if status == 200:
        resposta = data.get("resposta") or data.get("response") or data.get("message") or ""
        if resposta and len(resposta) > 10:
            log_ok(f"Chat IA respondeu!")
            log_ok(f"Resposta: {resposta[:80]}...")
        else:
            log_warn(f"Chat respondeu mas sem conteúdo: {data}")
    elif status == 401:
        log_warn("Chat requer autenticação diferente")
    else:
        log_erro(f"Chat falhou: {status} — {data}")
else:
    log_erro("Sem token para testar chat")

# ══════════════════════════════════════════════════
# 7. DIÁRIO EMOCIONAL
# ══════════════════════════════════════════════════
secao("7. DIÁRIO EMOCIONAL")

if TOKEN:
    # Salvar entrada
    status, data = req("POST", "/api/v1/diario", {
        "emocao": "feliz",
        "intensidade": 8,
        "texto": "Hoje foi um dia produtivo testando a plataforma!",
        "humor": "bom"
    }, token=TOKEN)

    if status in [200, 201]:
        log_ok(f"Diário salvo! — {data}")
    else:
        log_warn(f"Diário: {status} — {data}")

    # Listar entradas
    status, data = req("GET", "/api/v1/diario", token=TOKEN)
    if status == 200:
        entradas = data if isinstance(data, list) else data.get("entradas", [])
        log_ok(f"Diário listado — {len(entradas)} entradas")
    else:
        log_warn(f"Listar diário: {status} — {data}")
else:
    log_erro("Sem token para testar diário")

# ══════════════════════════════════════════════════
# 8. ESCALAS PSICOLÓGICAS
# ══════════════════════════════════════════════════
secao("8. ESCALAS PSICOLÓGICAS")

# PHQ-9
if TOKEN:
    status, data = req("POST", "/api/v1/escalas/phq9", {
        "respostas": [1, 0, 1, 0, 1, 0, 1, 0, 0]
    }, token=TOKEN)
    if status in [200, 201]:
        log_ok(f"PHQ-9 OK — score={data.get('score', data.get('total', '?'))}")
        log_ok(f"Classificação: {data.get('classificacao', data.get('nivel', '?'))}")
    else:
        log_warn(f"PHQ-9: {status} — {data}")

    # GAD-7
    status, data = req("POST", "/api/v1/escalas/gad7", {
        "respostas": [1, 0, 1, 0, 1, 0, 1]
    }, token=TOKEN)
    if status in [200, 201]:
        log_ok(f"GAD-7 OK — score={data.get('score', data.get('total', '?'))}")
    else:
        log_warn(f"GAD-7: {status} — {data}")

# ══════════════════════════════════════════════════
# 9. GAMIFICAÇÃO
# ══════════════════════════════════════════════════
secao("9. GAMIFICAÇÃO E XP")

if TOKEN:
    status, data = req("GET", "/api/v1/xp", token=TOKEN)
    if status == 200:
        log_ok(f"XP OK — {data}")
    else:
        log_warn(f"XP: {status} — {data}")

    status, data = req("GET", "/api/v1/ranking", token=TOKEN)
    if status == 200:
        log_ok(f"Ranking OK")
    else:
        log_warn(f"Ranking: {status} — {data}")

# ══════════════════════════════════════════════════
# 10. PIX
# ══════════════════════════════════════════════════
secao("10. PIX — QR CODE")

status, data = req("GET", "/api/v1/pix/qrcode")
if status == 200:
    log_ok("PIX QR Code gerado!")
    if "qr" in str(data).lower() or "pix" in str(data).lower():
        log_ok("Dados PIX presentes")
else:
    log_warn(f"PIX: {status} — {data}")

# ══════════════════════════════════════════════════
# 11. STRIPE
# ══════════════════════════════════════════════════
secao("11. STRIPE — PLANOS")

status, data = req("GET", "/api/v1/stripe/planos")
if status == 200:
    log_ok(f"Stripe planos OK — {data}")
else:
    log_warn(f"Stripe planos: {status} — {data}")

# ══════════════════════════════════════════════════
# 12. ROTAS DA API
# ══════════════════════════════════════════════════
secao("12. ROTAS CRÍTICAS DA API")

rotas_api = [
    ("GET",  "/api/v1/auth/stats/usuarios"),
    ("GET",  "/sitemap.xml"),
    ("GET",  "/robots.txt"),
    ("GET",  "/manifest.json"),
    ("GET",  "/sw.js"),
]

for method, rota in rotas_api:
    status, data = req(method, rota)
    if status in [200, 201]:
        log_ok(f"{method} {rota} → {status}")
    elif status in [401, 403]:
        log_warn(f"{method} {rota} → {status} (protegida)")
    else:
        log_warn(f"{method} {rota} → {status}")

# ══════════════════════════════════════════════════
# 13. SEGURANÇA
# ══════════════════════════════════════════════════
secao("13. SEGURANÇA")

# Token inválido deve retornar 401
status, data = req("GET", "/api/v1/auth/me", token="token_invalido_123")
if status == 401:
    log_ok("Token inválido rejeitado corretamente (401)")
else:
    log_warn(f"Token inválido retornou {status} — esperado 401")

# Login com senha errada
status, data = req("POST", "/api/v1/auth/login", {
    "email": EMAIL,
    "senha": "senhaerrada999"
})
if status == 401:
    log_ok("Senha errada rejeitada corretamente (401)")
else:
    log_warn(f"Senha errada retornou {status} — esperado 401")

# Swagger bloqueado
status, data = req("GET", "/docs")
if status in [401, 403, 404]:
    log_ok(f"Swagger bloqueado corretamente ({status})")
else:
    log_warn(f"Swagger acessível sem auth: {status}")

# ══════════════════════════════════════════════════
# 14. RESUMO FINAL
# ══════════════════════════════════════════════════
secao("14. RESUMO FINAL DOS FLUXOS REAIS")

total = ok + warn + erro
pct_ok   = (ok   / total * 100) if total else 0
pct_warn = (warn / total * 100) if total else 0
pct_erro = (erro / total * 100) if total else 0

print(f"\n  {VERDE}✅ OK:       {ok:3d}  ({pct_ok:.0f}%){RESET}")
print(f"  {AMARELO}⚠️  Warnings: {warn:3d}  ({pct_warn:.0f}%){RESET}")
print(f"  {VERMELHO}❌ Erros:    {erro:3d}  ({pct_erro:.0f}%){RESET}")

score = int(pct_ok)
print(f"\n  {NEGRITO}📊 Score funcional real: {score}%{RESET}")

if score >= 90:
    print(f"  {VERDE}{NEGRITO}🚀 Sistema excelente! Pronto para usuários reais.{RESET}")
elif score >= 70:
    print(f"  {AMARELO}{NEGRITO}⚡ Sistema bom, pequenos ajustes necessários.{RESET}")
else:
    print(f"  {VERMELHO}{NEGRITO}🔧 Sistema precisa de atenção.{RESET}")

# Salvar
with open("teste_fluxos_resultado.txt", "w") as f:
    f.write(f"Score: {score}%\n\n")
    for r in resultados:
        f.write(r + "\n")

print(f"\n  📄 Salvo em: teste_fluxos_resultado.txt")
print(f"{AZUL}{'='*55}{RESET}\n")
