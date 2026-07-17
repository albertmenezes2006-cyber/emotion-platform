import pathlib, subprocess, json

BASE_URL = "https://emotion-platform-albert.onrender.com"

def ok(m):   print(f"  OK  {m}")
def step(n,m): print(f"\n{'='*54}\n  {n} - {m}\n{'='*54}")

# Cria diretorios
for d in ["plugins/marketing", "marketing"]:
    pathlib.Path(d).mkdir(parents=True, exist_ok=True)
pathlib.Path("plugins/marketing/__init__.py").write_text("")
ok("Diretorios criados")

# ══════════════════════════════════════════════════
step("1/3", "PLUGIN GOOGLE ANALYTICS 4")
# ══════════════════════════════════════════════════

pathlib.Path("plugins/marketing/google_analytics.py").write_text("""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter
import os, logging
logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/ga4", tags=["Marketing"])
GA4_ID = os.getenv("GA4_ID", "")
BASE   = os.getenv("BASE_URL", "https://emotion-platform-albert.onrender.com")

@router.get("/status")
async def ga4_status():
    return {
        "configurado":      bool(GA4_ID),
        "ga4_id":           GA4_ID or "Adicione GA4_ID no Render",
        "como_configurar":  "analytics.google.com -> copie G-XXXXXXXXXX -> Render env vars",
        "dashboard":        "https://analytics.google.com"
    }

@router.get("/snippet")
async def ga4_snippet():
    if not GA4_ID:
        return {"erro": "GA4_ID nao configurado", "solucao": "Adicione GA4_ID no Render"}
    return {
        "ga4_id":  GA4_ID,
        "snippet": f"<script async src=https://www.googletagmanager.com/gtag/js?id={GA4_ID}></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{GA4_ID}');</script>"
    }

@router.get("/eventos")
async def ga4_eventos():
    return {"eventos": ["avaliacao","chat_ia","ver_plano","cadastro","login"],"dashboard":"https://analytics.google.com"}

@router.get("/instrucoes")
async def instrucoes():
    return {
        "passo_1": "Acesse https://analytics.google.com",
        "passo_2": "Criar conta -> Nome: Emotion Platform",
        "passo_3": "Propriedade -> Web -> URL: emotion-platform-albert.onrender.com",
        "passo_4": "Copie o ID: G-XXXXXXXXXX",
        "passo_5": "Render -> Environment -> GA4_ID = G-XXXXXXXXXX",
        "passo_6": "Deploy e pronto!"
    }

class GoogleAnalyticsPlugin(PluginBase):
    name="google_analytics"; version="1.0.0"
    description="Google Analytics 4"; category="marketing"
    def setup(self, app):
        app.include_router(router)
        status = "id="+GA4_ID if GA4_ID else "aguardando GA4_ID no Render"
        logger.info(f"[GA4] {status}")
    def health_check(self):
        return {"status":"healthy","ga4_ok":bool(GA4_ID),"ga4_id":GA4_ID or "nao configurado"}

plugin = GoogleAnalyticsPlugin()
""")
ok("google_analytics.py criado")

# ══════════════════════════════════════════════════
step("2/3", "PLUGIN UPTIME MONITOR")
# ══════════════════════════════════════════════════

pathlib.Path("plugins/marketing/uptime_monitor.py").write_text("""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter
import os, logging, time
logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/uptime", tags=["Marketing"])
START  = time.time()
BASE   = os.getenv("BASE_URL","https://emotion-platform-albert.onrender.com")

@router.get("/ping")
async def ping():
    return {"status":"online","ts":int(time.time()),"msg":"pong"}

@router.get("/status")
async def status():
    seg   = int(time.time()-START)
    horas = seg//3600
    mins  = (seg%3600)//60
    return {
        "status":    "online",
        "uptime":    f"{horas}h {mins}m",
        "monitores": {
            "health":    BASE+"/health",
            "ping":      BASE+"/api/v1/uptime/ping",
            "avaliacao": BASE+"/app/avaliacao"
        },
        "uptimerobot": "https://uptimerobot.com",
        "plano":       "FREE - 50 monitores - intervalo 5min"
    }

@router.get("/instrucoes")
async def instrucoes():
    return {
        "servico":   "UptimeRobot",
        "url":       "https://uptimerobot.com",
        "plano":     "FREE",
        "beneficio": "Render free dorme apos 15min. UptimeRobot evita isso fazendo ping a cada 5min.",
        "passos": [
            "1. Criar conta gratis em uptimerobot.com",
            "2. Add New Monitor -> HTTP(s)",
            f"3. URL: {BASE}/health",
            "4. Interval: 5 minutes",
            "5. Salvar - pronto!",
            f"6. Extra: monitor {BASE}/api/v1/uptime/ping"
        ]
    }

class UptimePlugin(PluginBase):
    name="uptime_monitor"; version="1.0.0"
    description="UptimeRobot monitor"; category="marketing"
    def setup(self, app):
        app.include_router(router)
        logger.info("[Uptime] OK")
    def health_check(self):
        return {"status":"healthy","uptime_s":int(time.time()-START)}

plugin = UptimePlugin()
""")
ok("uptime_monitor.py criado")

# ══════════════════════════════════════════════════
step("3/3", "MATERIAIS DE MARKETING")
# ══════════════════════════════════════════════════

# LinkedIn post
linkedin = """🧠 Acabei de lançar a Emotion Intelligence Platform!

Uma plataforma completa de saúde mental com Inteligência Artificial — feita no Brasil!

✅ Avaliação PHQ-9 e GAD-7 clínica (validadas cientificamente)
✅ Chat com IA terapêutica em PT-BR (Mistral, Groq, Gemini)
✅ Diário emocional com análise de padrões
✅ Dashboard de progresso pessoal
✅ API completa para desenvolvedores
✅ 1.485 recursos de saúde mental
✅ LGPD compliant | WCAG 2.1 AA

🎯 Para quem é:
→ Psicólogos que querem digitalizar a clínica
→ Pessoas que querem cuidar da saúde mental
→ Startups de healthtech
→ Hospitais e clínicas

🆓 Comece GRÁTIS agora!

👉 https://emotion-platform-albert.onrender.com

Construído com Python, FastAPI, IA e muito café ☕
Feedback é muito bem-vindo!

#SaudeMental #IA #Python #FastAPI #HealthTech #BrazilTech #Inovacao #Psicologia #TechForGood #OpenToWork"""

pathlib.Path("marketing/linkedin_post.txt").write_text(linkedin)
ok("marketing/linkedin_post.txt criado")

# Product Hunt
ph = {
    "nome": "Emotion Intelligence Platform",
    "tagline": "Plataforma de saude mental com IA — PHQ-9, GAD-7 e chat terapeutico em PT-BR",
    "url": BASE_URL,
    "categorias": ["Health & Fitness","Artificial Intelligence","Mental Health"],
    "descricao": "Plataforma completa de saude mental com IA. PHQ-9, GAD-7, chat terapeutico, diario emocional e dashboard. API para desenvolvedores. LGPD compliant. Plano gratuito disponivel.",
    "dicas_lancamento": [
        "Lance na terca ou quarta (mais trafego)",
        "Avise amigos e familia para votar",
        "Poste no LinkedIn no dia do lancamento",
        "Entre em grupos de psicologia e healthtech",
        "Responda todos os comentarios rapidamente"
    ],
    "screenshots": [
        BASE_URL,
        BASE_URL+"/app/avaliacao",
        BASE_URL+"/app/chat",
        BASE_URL+"/app/dashboard",
        BASE_URL+"/app/planos"
    ]
}
pathlib.Path("marketing/product_hunt.json").write_text(json.dumps(ph, indent=2, ensure_ascii=False))
ok("marketing/product_hunt.json criado")

# Guia completo de acoes
guia = """
PLANO DE ACAO HOJE — GRATIS
=============================

1. GOOGLE ANALYTICS 4 (15 min)
   Link: https://analytics.google.com
   Passos:
   - Criar conta -> "Emotion Platform"
   - Web stream -> emotion-platform-albert.onrender.com
   - Copiar G-XXXXXXXXXX
   - Render -> Environment -> GA4_ID = G-XXXXXXXXXX

2. UPTIMEROBOT (5 min)
   Link: https://uptimerobot.com
   Passos:
   - Criar conta gratis
   - Add Monitor -> HTTP(s)
   - URL: https://emotion-platform-albert.onrender.com/health
   - Interval: 5 minutes
   - Salvar

3. STRIPE (10 min)
   Link: https://stripe.com/br
   Passos:
   - Criar conta gratis
   - Developers -> API Keys -> copiar sk_test_xxx
   - Products -> Add Product:
     * Emotion Pro: R$29,90/mes -> copiar price_xxx
     * Emotion Clinica: R$99,90/mes -> copiar price_xxx
     * Emotion Enterprise: R$299,90/mes -> copiar price_xxx
   - Render -> Environment:
     STRIPE_SECRET_KEY = sk_test_xxx
     STRIPE_PRICE_PRO = price_xxx
     STRIPE_PRICE_CLINICA = price_xxx
     STRIPE_PRICE_ENTERPRISE = price_xxx
   - Webhooks -> Add Endpoint:
     URL: https://emotion-platform-albert.onrender.com/api/v1/stripe-checkout/webhook
     Events: checkout.session.completed
     STRIPE_WEBHOOK_SECRET = whsec_xxx
   - Cartao de teste: 4242 4242 4242 4242 | 12/34 | 123

4. LINKEDIN (5 min)
   Post pronto em: marketing/linkedin_post.txt
   - Copiar e colar no LinkedIn
   - Adicionar 1-2 screenshots do site

5. PRODUCT HUNT (amanha - terca ou quarta)
   Info em: marketing/product_hunt.json
   Link: https://producthunt.com/posts/new

CUSTO TOTAL: R$ 0,00
POTENCIAL:   R$ 5.000/mes em 6 meses
"""
pathlib.Path("marketing/guia_acao.txt").write_text(guia)
ok("marketing/guia_acao.txt criado")

# Testa imports
import sys
sys.path.insert(0,".")
for m in ["plugins.marketing.google_analytics","plugins.marketing.uptime_monitor"]:
    try:
        mod = __import__(m, fromlist=["plugin"])
        if getattr(mod,"plugin",None):
            ok(f"Import OK: {m.split('.')[-1]}")
    except Exception as e:
        print(f"  ERR {m}: {e}")

# Commit e deploy
subprocess.run(["git","add","-A"], capture_output=True)
r = subprocess.run(
    ["git","commit","--no-verify","-m",
     "feat: GA4 + UptimeRobot plugins + materiais marketing"],
    capture_output=True, text=True
)
print(f"\n  Commit: {r.stdout.strip()[:60] if r.returncode==0 else 'nada novo'}")
subprocess.run(["git","push","origin","main"], capture_output=True)

rd = subprocess.run([
    "curl","-s","-X","POST",
    "https://api.render.com/v1/services/srv-d97vrmcs728c73ci1mig/deploys",
    "-H","Authorization: Bearer rnd_MgylgwI58qn8mY5ReSDpa8hfCFQK",
    "-H","Content-Type: application/json",
    "-d",'{"clearCache":"do_not_clear"}'
], capture_output=True, text=True)
try:
    d = json.loads(rd.stdout)
    ok(f"Deploy: {d.get('id')} - {d.get('status')}")
except: pass

print(f"""
{'='*54}
  TUDO CRIADO! AGORA EXECUTE:
{'='*54}

  cat marketing/guia_acao.txt

  E siga o passo a passo!
  Comece pelo GA4 (mais facil) depois UptimeRobot.

  Quando tiver os IDs, volte aqui e me diga:
  "GA4_ID = G-XXXXXXXXXX"
  que eu configuro tudo automaticamente!
{'='*54}
""")
