#!/usr/bin/env python3
"""
Teste de Fluxos Reais v2 — rotas corrigidas
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

BASE  = "https://emotion-platform-albert.onrender.com"
TOKEN = None
EMAIL = f"teste_{''.join(random.choices(string.ascii_lowercase, k=6))}@teste.com"
SENHA = "senha123"

ok = 0; warn = 0; erro = 0
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

def req(method, path, body=None, token=None):
    url = BASE + path
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    data = json.dumps(body).encode() if body else None
    try:
        r = urllib.request.Request(url, data=data, headers=headers, method=method)
        with urllib.request.urlopen(r, timeout=30) as resp:
            try:
                return resp.status, json.loads(resp.read())
            except:
                return resp.status, {}
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read())
        except:
            return e.code, {}
    except Exception as ex:
        return 0, {"erro": str(ex)}

# ══════════════════════════════════════════════════
# 1. HEALTH
# ══════════════════════════════════════════════════
secao("1. HEALTH CHECK")
status, data = req("GET", "/health")
if status == 200:
    log_ok(f"Online! plugins={data.get('plugins')} rotas={data.get('rotas')} erros={data.get('erros')}")
else:
    log_erro(f"Offline: {status}")

# ══════════════════════════════════════════════════
# 2. PÁGINAS HTML — rotas reais
# ══════════════════════════════════════════════════
secao("2. PÁGINAS HTML — ROTAS REAIS")

paginas = [
    # Públicas
    ("/",                    "Home"),
    ("/app/login",           "Login"),
    ("/app/cadastro",        "Cadastro"),
    ("/sobre",               "Sobre"),
    ("/precos",              "Preços"),
    ("/premium",             "Premium"),
    ("/blog",                "Blog"),
    ("/faq",                 "FAQ"),
    ("/contato",             "Contato"),
    ("/privacidade-lgpd",    "Privacidade"),
    ("/termos-uso",          "Termos"),
    ("/psicologos",          "Psicólogos"),
    ("/para-psicologos",     "Para Psicólogos"),
    ("/para-clinicas",       "Para Clínicas"),
    ("/whitelabel",          "Whitelabel"),
    ("/afiliado",            "Afiliado"),
    ("/emergencia",          "Emergência"),
    # App
    ("/app/dashboard",       "Dashboard"),
    ("/app/chat",            "Chat IA"),
    ("/app/diario",          "Diário"),
    ("/app/avaliacao",       "Avaliação"),
    ("/app/analises",        "Análises"),
    ("/app/carteira",        "Carteira"),
    ("/app/score-ie",        "Score IE"),
    ("/app/planos",          "Planos"),
    # Checkout
    ("/checkout/anual",      "Checkout Anual"),
    ("/checkout/api",        "Checkout API"),
    ("/checkout/creditos",   "Checkout Créditos"),
    ("/checkout/relatorio",  "Checkout Relatório"),
    ("/checkout/sofia",      "Checkout Sofia"),
    # Outras
    ("/nova-senha",          "Nova Senha"),
    ("/presente/sucesso",    "Presente Sucesso"),
    ("/offline",             "Offline"),
    ("/sitemap.xml",         "Sitemap"),
    ("/robots.txt",          "Robots"),
    ("/respiracao",          "Respiração"),
    ("/meditacao",           "Meditação"),
    ("/gratidao",            "Gratidão"),
    ("/grounding",           "Grounding"),
    ("/onboarding",          "Onboarding"),
]

pag_ok = 0; pag_err = 0
for rota, nome in paginas:
    status, _ = req("GET", rota)
    if status == 200:
        pag_ok += 1
    elif status in [401, 403]:
        log_warn(f"Protegida: {nome} ({rota})")
    elif status == 404:
        log_erro(f"404: {nome} ({rota})")
        pag_err += 1
    elif status == 500:
        log_erro(f"500: {nome} ({rota})")
        pag_err += 1
    else:
        log_warn(f"{status}: {nome} ({rota})")

log_ok(f"Páginas OK: {pag_ok}/{len(paginas)}")
if pag_err > 0:
    log_erro(f"Páginas com erro: {pag_err}")

# ══════════════════════════════════════════════════
# 3. CADASTRO
# ══════════════════════════════════════════════════
secao("3. CADASTRO")
status, data = req("POST", "/api/v1/auth/cadastrar", {
    "nome": "Teste Albert",
    "email": EMAIL,
    "senha": SENHA,
    "tipo": "paciente"
})
if status in [200, 201]:
    TOKEN = data.get("token") or data.get("access_token")
    log_ok(f"Cadastro OK — user_id={data.get('user_id')}")
    log_ok(f"Token: {'✅' if TOKEN else '❌'}")
    log_ok(f"Plano: {data.get('plano')} | Tipo: {data.get('tipo')}")
else:
    log_erro(f"Cadastro falhou: {status} — {data}")

# ══════════════════════════════════════════════════
# 4. LOGIN
# ══════════════════════════════════════════════════
secao("4. LOGIN")
status, data = req("POST", "/api/v1/auth/login", {
    "email": EMAIL, "senha": SENHA
})
if status == 200:
    TOKEN = data.get("token") or data.get("access_token")
    log_ok(f"Login OK — {data.get('status')}")
    log_ok(f"Token: {'✅' if TOKEN else '❌'}")
    log_ok(f"Nome: {data.get('nome')} | Tipo: {data.get('tipo')}")
else:
    log_erro(f"Login falhou: {status} — {data}")

# ══════════════════════════════════════════════════
# 5. TOKEN /me
# ══════════════════════════════════════════════════
secao("5. VERIFICAÇÃO DE TOKEN")
if TOKEN:
    status, data = req("GET", "/api/v1/auth/me", token=TOKEN)
    if status == 200:
        log_ok(f"Token válido — {data.get('nome')} / {data.get('email')}")
    else:
        log_erro(f"Token inválido: {status}")
else:
    log_erro("Sem token!")

# ══════════════════════════════════════════════════
# 6. CHAT IA
# ══════════════════════════════════════════════════
secao("6. CHAT IA (Mistral)")
if TOKEN:
    # Rota real: /api/v1/chat/enviar
    status, data = req("POST", "/api/v1/chat/enviar", {
        "mensagem": "Olá! Como posso melhorar minha saúde mental?"
    }, token=TOKEN)
    if status == 200:
        resposta = data.get("resposta") or data.get("response") or data.get("message") or str(data)
        log_ok(f"Chat IA OK!")
        log_ok(f"Resposta: {str(resposta)[:100]}...")
    else:
        # Tentar rota alternativa
        status2, data2 = req("POST", "/api/v1/chat-ia/mensagem", {
            "mensagem": "Olá!"
        }, token=TOKEN)
        if status2 == 200:
            log_ok(f"Chat IA OK (rota alternativa)!")
        else:
            log_warn(f"Chat: {status} | Alt: {status2} — {data}")

# ══════════════════════════════════════════════════
# 7. DIÁRIO
# ══════════════════════════════════════════════════
secao("7. DIÁRIO EMOCIONAL")
if TOKEN:
    # Rota real: /api/v1/diario/salvar
    status, data = req("POST", "/api/v1/diario/salvar", {
        "emocao": "feliz",
        "intensidade": 8,
        "texto": "Testando o diário!",
        "humor": "bom"
    }, token=TOKEN)
    if status in [200, 201]:
        log_ok(f"Diário salvo!")
    else:
        # Tentar rota alternativa
        status2, data2 = req("POST", "/api/v1/diario-emocional/entrada", {
            "emocao": "feliz", "texto": "Teste"
        }, token=TOKEN)
        if status2 in [200, 201]:
            log_ok("Diário salvo (rota alternativa)!")
        else:
            log_warn(f"Diário: {status} | Alt: {status2}")

# ══════════════════════════════════════════════════
# 8. ESCALAS
# ══════════════════════════════════════════════════
secao("8. ESCALAS PSICOLÓGICAS")
if TOKEN:
    # PHQ-9 — rota real: /api/v1/phq9/calcular
    status, data = req("POST", "/api/v1/phq9/calcular", {
        "respostas": [1, 0, 1, 0, 1, 0, 1, 0, 0]
    }, token=TOKEN)
    if status in [200, 201]:
        log_ok(f"PHQ-9 OK — score={data.get('score', data.get('total', '?'))}")
        log_ok(f"Nível: {data.get('classificacao', data.get('nivel', data.get('interpretacao', '?')))}")
    else:
        log_warn(f"PHQ-9: {status} — {data}")

    # PSS — rota real: /api/v1/pss/calcular
    status, data = req("POST", "/api/v1/pss/calcular", [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], token=TOKEN)
    if status in [200, 201]:
        log_ok(f"PSS OK — {data}")
    else:
        log_warn(f"PSS: {status}")

# ══════════════════════════════════════════════════
# 9. GAMIFICAÇÃO
# ══════════════════════════════════════════════════
secao("9. GAMIFICAÇÃO E XP")
if TOKEN:
    # Rota real: /api/v1/xp/ganhar
    status, data = req("POST", "/api/v1/xp/ganhar?user_id=" + (localStorage_userid if locals().get("localStorage_userid") else "test123") + "&acao=diario_salvo&xp=10")
    if status in [200, 201]:
        log_ok(f"XP ganho! — {data}")
    else:
        log_warn(f"XP ganhar: {status}")

    # Ranking: /api/v1/xp/ranking/top
    status, data = req("GET", "/api/v1/xp/ranking/top")
    if status == 200:
        log_ok(f"Ranking OK!")
    else:
        log_warn(f"Ranking: {status}")

# ══════════════════════════════════════════════════
# 10. PIX
# ══════════════════════════════════════════════════
secao("10. PIX")
status, data = req("GET", "/qr/")
if status == 200:
    log_ok("PIX/QR OK!")
else:
    status2, data2 = req("GET", "/qr/site")
    if status2 == 200:
        log_ok("PIX/QR OK (rota alternativa)!")
    else:
        log_warn(f"PIX: {status} | Alt: {status2}")

# ══════════════════════════════════════════════════
# 11. STRIPE
# ══════════════════════════════════════════════════
secao("11. STRIPE")
status, data = req("GET", "/api/v1/stripe/planos")
if status == 200:
    planos = list(data.get("planos", {}).keys())
    log_ok(f"Stripe OK — planos: {planos}")
else:
    log_warn(f"Stripe: {status}")

# ══════════════════════════════════════════════════
# 12. PWA
# ══════════════════════════════════════════════════
secao("12. PWA")
for rota in ["/manifest.json", "/sw.js", "/offline"]:
    status, _ = req("GET", rota)
    if status == 200:
        log_ok(f"PWA {rota} OK!")
    else:
        log_warn(f"PWA {rota}: {status}")

# ══════════════════════════════════════════════════
# 13. SEGURANÇA
# ══════════════════════════════════════════════════
secao("13. SEGURANÇA")

status, _ = req("GET", "/api/v1/auth/me", token="token_invalido")
if status == 401:
    log_ok("Token inválido rejeitado (401) ✅")
else:
    log_warn(f"Token inválido retornou {status}")

status, _ = req("POST", "/api/v1/auth/login", {
    "email": EMAIL, "senha": "senhaerrada"
})
if status == 401:
    log_ok("Senha errada rejeitada (401) ✅")
else:
    log_warn(f"Senha errada retornou {status}")

status, _ = req("GET", "/docs")
if status in [401, 403, 404]:
    log_ok(f"Swagger bloqueado ({status}) ✅")
else:
    log_warn(f"Swagger acessível: {status}")

# ══════════════════════════════════════════════════
# 14. TELEGRAM
# ══════════════════════════════════════════════════
secao("14. TELEGRAM")
status, data = req("GET", "/api/v1/telegram/setup")
if status == 200:
    log_ok(f"Telegram configurado!")
else:
    log_warn(f"Telegram: {status}")

# ══════════════════════════════════════════════════
# RESUMO
# ══════════════════════════════════════════════════
secao("RESUMO FINAL")
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
    print(f"  {VERDE}{NEGRITO}🚀 Excelente! Pronto para usuários reais.{RESET}")
elif score >= 70:
    print(f"  {AMARELO}{NEGRITO}⚡ Bom! Pequenos ajustes necessários.{RESET}")
else:
    print(f"  {VERMELHO}{NEGRITO}🔧 Precisa de atenção.{RESET}")

with open("teste_v2_resultado.txt", "w") as f:
    f.write(f"Score: {score}%\n\n")
    for r in resultados:
        f.write(r + "\n")

print(f"\n  📄 Salvo em: teste_v2_resultado.txt")
print(f"{AZUL}{'='*55}{RESET}\n")
