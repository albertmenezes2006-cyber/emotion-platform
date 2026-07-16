#!/usr/bin/env python3
"""Análise profunda de TUDO no site"""
import urllib.request, json, time

BASE = "https://emotion-platform-albert.onrender.com"

def get(path, t=30):
    try:
        with urllib.request.urlopen(BASE+path, timeout=t) as r:
            body = r.read().decode()
            return r.status, body
    except Exception as e:
        return 0, str(e)[:100]

def post(path, data=None, t=40):
    try:
        payload = json.dumps(data or {}).encode()
        req = urllib.request.Request(BASE+path, data=payload, method="POST")
        req.add_header("Content-Type", "application/json")
        with urllib.request.urlopen(req, timeout=t) as r:
            return r.status, json.loads(r.read().decode())
    except Exception as e:
        return 0, {"error": str(e)[:100]}

print("="*60)
print("ANÁLISE PROFUNDA DO SITE")
print("="*60)

# ══════════════════════════════════════════
# 1. HEALTH GERAL
# ══════════════════════════════════════════
print("\n1. SISTEMA")
s, body = get("/health")
if s == 200:
    d = json.loads(body)
    print(f"   Versão: {d.get('version')}")
    print(f"   Plugins: {d.get('plugins')}")
    print(f"   Rotas: {d.get('rotas')}")
    print(f"   Uptime: {d.get('uptime')}")
else:
    print(f"   ❌ Health falhou: {s}")

# ══════════════════════════════════════════
# 2. PÁGINAS — ANÁLISE DETALHADA
# ══════════════════════════════════════════
print("\n2. PÁGINAS HTML")
paginas = [
    ("/",              "Home"),
    ("/app/avaliacao", "Avaliação PHQ-9/GAD-7"),
    ("/app/chat",      "Chat IA"),
    ("/app/diario",    "Diário Emocional"),
    ("/app/dashboard", "Dashboard"),
    ("/app/planos",    "Planos"),
    ("/app/login",     "Login/Cadastro"),
    ("/docs",          "API Docs Swagger"),
]
for path, nome in paginas:
    s, body = get(path)
    if s == 200:
        size = len(body)
        # Verificar elementos chave
        tem_nav = "nav" in body.lower()
        tem_css = "emotion.css" in body or "style" in body
        tem_js = "<script" in body
        tem_api = "fetch(" in body or "api/v1" in body
        is_swagger = "swagger" in body.lower()
        is_real = size > 5000
        
        problemas = []
        if not tem_nav and not is_swagger: problemas.append("sem nav")
        if not tem_css and not is_swagger: problemas.append("sem css")
        if not is_real: problemas.append(f"pequena ({size}b)")
        
        status = "✅" if not problemas and is_real else "⚠️"
        print(f"   {status} {nome}: {size:,}b | nav={tem_nav} css={tem_css} js={tem_js} api={tem_api}")
        if problemas:
            print(f"      ⚠️  Problemas: {', '.join(problemas)}")
    else:
        print(f"   ❌ {nome}: HTTP {s}")

# ══════════════════════════════════════════
# 3. TESTAR CHAT IA — MÚLTIPLAS PERGUNTAS
# ══════════════════════════════════════════
print("\n3. CHAT IA — TESTE REAL")
perguntas_chat = [
    ("Olá, como você pode me ajudar?", "saudação"),
    ("Estou com ansiedade, o que faço?", "ansiedade"),
    ("Me ensina respiração 4-7-8", "técnica"),
    ("Estou muito triste hoje", "tristeza"),
    ("O que é TCC?", "psicoeducação"),
]
chat_ok = 0
for msg, tipo in perguntas_chat:
    s, d = post(f"/api/v1/chat-ia/mensagem?user_id=analise&mensagem={msg.replace(' ','+')}",{})
    modelo = d.get("modelo_usado","?")
    resp = str(d.get("resposta",""))
    ok = s==200 and len(resp) > 20 and modelo != "?"
    if ok: chat_ok += 1
    print(f"   {'✅' if ok else '❌'} [{tipo}] modelo={modelo}")
    print(f"      Resp: {resp[:80]}...")
    time.sleep(0.5)

print(f"   Chat: {chat_ok}/{len(perguntas_chat)} OK")

# ══════════════════════════════════════════
# 4. PHQ-9 E GAD-7
# ══════════════════════════════════════════
print("\n4. ESCALAS CLÍNICAS")

# PHQ-9 perguntas
s, body = get("/api/v1/phq9-clinico/perguntas")
if s == 200:
    d = json.loads(body)
    print(f"   ✅ PHQ-9 perguntas: {len(d.get('perguntas',[]))} questões")
else:
    print(f"   ❌ PHQ-9 perguntas: {s}")

# PHQ-9 aplicar
s, d = post("/api/v1/phq9-clinico/aplicar?user_id=analise", [2,1,2,1,0,1,2,0,0])
if s == 200:
    print(f"   ✅ PHQ-9 aplicar: score={d.get('score')} nivel={d.get('classificacao',{}).get('nivel')}")
else:
    print(f"   ❌ PHQ-9 aplicar: {s} {str(d)[:60]}")

# GAD-7 perguntas
s, body = get("/api/v1/gad7-clinico/perguntas")
if s == 200:
    d = json.loads(body)
    print(f"   ✅ GAD-7 perguntas: {len(d.get('perguntas',[]))} questões")
else:
    print(f"   ❌ GAD-7 perguntas: {s}")

# GAD-7 aplicar
s, d = post("/api/v1/gad7-clinico/aplicar?user_id=analise", [1,2,1,2,1,0,1])
if s == 200:
    print(f"   ✅ GAD-7 aplicar: score={d.get('score')} nivel={d.get('nivel')}")
else:
    print(f"   ❌ GAD-7 aplicar: {s} {str(d)[:60]}")

# ══════════════════════════════════════════
# 5. AUTH JWT
# ══════════════════════════════════════════
print("\n5. AUTENTICAÇÃO")
email_teste = f"analise_{int(time.time())}@test.com"

s, d = post(f"/api/v1/auth/cadastrar?nome=Analise&email={email_teste}&senha=Test1234&tipo=paciente")
if s == 200:
    token = d.get("token","")
    print(f"   ✅ Cadastro: user_id={d.get('user_id')} plano={d.get('plano')}")
    print(f"   ✅ Token: {token[:50]}...")
    
    # Login
    s2, d2 = post(f"/api/v1/auth/login?email={email_teste}&senha=Test1234")
    if s2 == 200:
        print(f"   ✅ Login: {d2.get('status')} plano={d2.get('user',{}).get('plano')}")
    else:
        print(f"   ❌ Login: {s2}")
    
    # Me
    try:
        req = urllib.request.Request(BASE+"/api/v1/auth/me")
        req.add_header("Authorization", "Bearer " + token)
        with urllib.request.urlopen(req, timeout=15) as r:
            d3 = json.loads(r.read().decode())
            print(f"   ✅ /me: email={d3.get('email')} plano={d3.get('plano')}")
    except Exception as e:
        print(f"   ❌ /me: {e}")
else:
    print(f"   ❌ Cadastro: {s} {str(d)[:80]}")

# ══════════════════════════════════════════
# 6. STRIPE E MONETIZAÇÃO
# ══════════════════════════════════════════
print("\n6. MONETIZAÇÃO")
s, body = get("/api/v1/stripe/planos")
if s == 200:
    d = json.loads(body)
    for nome, info in d.get("planos",{}).items():
        preco = info.get("preco_brl_formatted","?")
        popular = "⭐" if info.get("popular") else ""
        print(f"   ✅ {nome}: {preco} {popular}")
else:
    print(f"   ❌ Stripe planos: {s}")

s2, d2 = get("/api/v1/stripe/mrr")
if s2 == 200:
    print(f"   ✅ MRR: {d2.get('mrr_brl','?')}")
else:
    print(f"   ❌ MRR: {s2}")

# ══════════════════════════════════════════
# 7. DIÁRIO EMOCIONAL
# ══════════════════════════════════════════
print("\n7. DIÁRIO EMOCIONAL")
s, d = post("/api/v1/diario-emocional/entrada?user_id=analise&texto=Teste+da+analise&emocao_principal=alegria&intensidade=7&humor_geral=8")
print(f"   {'✅' if s==200 else '❌'} Criar entrada: {s} status={d.get('status','?')}")

s2, d2 = get("/api/v1/diario-emocional/emocoes/disponiveis")
if s2 == 200:
    print(f"   ✅ Emoções: {len(d2.get('emocoes',{}))} disponíveis")

s3, d3 = get("/api/v1/diario-emocional/historico/analise")
print(f"   {'✅' if s3==200 else '❌'} Histórico: {s3} total={d3.get('total_entradas',0)}")

# ══════════════════════════════════════════
# 8. MOBILE API
# ══════════════════════════════════════════
print("\n8. MOBILE API")
s, body = get("/api/mobile/v1/sdk/config")
if s == 200:
    d = json.loads(body)
    print(f"   ✅ SDK Config: {len(d.get('endpoints',{}))} endpoints")

s2, body2 = get("/api/mobile/v1/init?platform=ios&app_version=1.0")
print(f"   {'✅' if s2==200 else '❌'} Init mobile: {s2}")

s3, d3 = get("/api/mobile/v1/home/analise")
if s3 == 200:
    print(f"   ✅ Home mobile: {d3.get('saudacao')} | {len(d3.get('widgets',[]))} widgets")

# ══════════════════════════════════════════
# 9. MULTI-LLM
# ══════════════════════════════════════════
print("\n9. MULTI-LLM")
s, body = get("/api/v1/multi-llm/modelos")
if s == 200:
    d = json.loads(body)
    for m in d.get("modelos",[]):
        disp = "✅" if m.get("disponivel") else "❌"
        print(f"   {disp} {m.get('nome')}: {m.get('velocidade','?')}")

s2, d2 = post("/api/v1/multi-llm/chat?mensagem=Ola+como+esta&user_id=analise")
print(f"   {'✅' if s2==200 else '❌'} Multi-LLM chat: modelo={d2.get('modelo_usado')}")
print(f"      {str(d2.get('resposta',''))[:80]}")

# ══════════════════════════════════════════
# 10. OUTROS ENDPOINTS IMPORTANTES
# ══════════════════════════════════════════
print("\n10. OUTROS ENDPOINTS")
outros = [
    ("/api/v1/auth/stats/usuarios","Auth stats"),
    ("/api/v1/monitor/status-completo","Monitor"),
    ("/api/v1/monitor/ping","Ping"),
    ("/api/mobile/v1/feed/analise","Feed mobile"),
    ("/api/v1/multi-llm/modelos","Multi-LLM modelos"),
]
for path, nome in outros:
    s, body = get(path)
    ok = s == 200
    print(f"   {'✅' if ok else '❌'} {nome}: {s}")

# ══════════════════════════════════════════
# 11. ANÁLISE DO CSS E FRONTEND
# ══════════════════════════════════════════
print("\n11. ASSETS E CSS")
s, body = get("/static/css/emotion.css")
if s == 200:
    print(f"   ✅ emotion.css: {len(body):,} chars")
    # Verificar variáveis CSS
    tem_primary = "--primary" in body
    tem_gradient = "--gradient" in body
    tem_nav = ".nav" in body
    tem_btn = ".btn" in body
    print(f"      vars: primary={tem_primary} gradient={tem_gradient} nav={tem_nav} btn={tem_btn}")
else:
    print(f"   ❌ CSS não carrega: {s}")

# ══════════════════════════════════════════
# RESUMO FINAL
# ══════════════════════════════════════════
print("\n" + "="*60)
print("RESUMO DA ANÁLISE")
print("="*60)

# Verificar o que está realmente quebrando no front
print("\nPROBLEMAS DETECTADOS:")
problemas_encontrados = []

# Verificar se home mostra swagger (errado)
s_home, body_home = get("/")
if "swagger" in body_home.lower() and "EmotionAI" not in body_home:
    problemas_encontrados.append("❌ HOME mostra Swagger em vez da página real")
elif len(body_home) < 5000:
    problemas_encontrados.append(f"❌ HOME pequena demais ({len(body_home)} chars)")
else:
    print("   ✅ Home OK")

# Verificar chat
s_chat, body_chat = get("/app/chat")
if "fetch(" not in body_chat:
    problemas_encontrados.append("❌ CHAT sem chamadas API no JS")
elif "/api/v1/chat-ia" not in body_chat:
    problemas_encontrados.append("❌ CHAT usa endpoint errado")
else:
    print("   ✅ Chat OK")

# Verificar avaliacao
s_av, body_av = get("/app/avaliacao")
if "phq9-clinico" not in body_av and "phq9" not in body_av.lower():
    problemas_encontrados.append("❌ AVALIAÇÃO não aponta para endpoint correto")
else:
    print("   ✅ Avaliação OK")

if problemas_encontrados:
    for p in problemas_encontrados:
        print(f"   {p}")
else:
    print("   ✅ Nenhum problema crítico detectado!")

print(f"\nSite: {BASE}")
print(f"Total de análises: concluída")
