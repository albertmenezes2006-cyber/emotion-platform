"""Plugin: Frontend Routes — serve páginas HTML"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, RedirectResponse
from datetime import datetime
import os, logging

logger = logging.getLogger(__name__)
router = APIRouter(tags=["frontend"])

def read_template(name):
    """Lê template HTML do disco"""
    paths = [
        f"templates/{name}",
        f"templates/{name}.html",
    ]
    for path in paths:
        if os.path.exists(path):
            try:
                with open(path, encoding="utf-8") as f:
                    return f.read()
            except Exception as e:
                logger.warning(f"Erro ao ler {path}: {e}")
    return None

class FrontendRoutesPlugin(PluginBase):
    name = "frontend_routes"
    version = "3.0.0"
    description = "Serve páginas HTML da plataforma"
    category = "frontend"

    def setup(self, app):
        # Montar static files
        try:
            from fastapi.staticfiles import StaticFiles
            if os.path.exists("static"):
                try:
                    app.mount("/static", StaticFiles(directory="static"), name="static_ep")
                except Exception:
                    pass
        except Exception:
            pass

        app.include_router(router)
        logger.info("[frontend_routes] OK")

    def health_check(self):
        templates = []
        if os.path.exists("templates"):
            templates = os.listdir("templates")
        return {"status": "healthy", "templates": len(templates)}

@router.get("/", response_class=HTMLResponse)
async def home():
    html = read_template("index.html") or read_template("index_new.html")
    if html:
        return HTMLResponse(html)
    return HTMLResponse("""<!DOCTYPE html>
<html lang="pt-BR">
<head><meta charset="UTF-8"><title>EmotionAI</title>
<style>*{margin:0;padding:0;box-sizing:border-box}body{font-family:system-ui;background:#09090B;color:#fff;min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center}h1{font-size:3rem;background:linear-gradient(135deg,#7C3AED,#EC4899);-webkit-background-clip:text;-webkit-text-fill-color:transparent}p{color:#A1A1AA;margin:1rem 0}a{color:#A78BFA;text-decoration:none}</style>
</head>
<body>
<div>
<h1>🧠 EmotionAI</h1>
<p>Plataforma de saúde mental com IA</p>
<p><a href="/app/avaliacao">🧪 Avaliação</a> · <a href="/app/chat">💬 Chat IA</a> · <a href="/docs">📚 Docs</a></p>
</div>
</body>
</html>""")

@router.get("/app/avaliacao", response_class=HTMLResponse)
async def avaliacao():
    html = read_template("avaliacao.html")
    if html:
        return HTMLResponse(html)
    return RedirectResponse("/docs")

@router.get("/app/chat", response_class=HTMLResponse)
async def chat():
    html = read_template("chat_ia.html")
    if html:
        return HTMLResponse(html)
    return RedirectResponse("/docs")

@router.get("/app/diario", response_class=HTMLResponse)
async def diario():
    html = read_template("diario.html")
    if html:
        return HTMLResponse(html)
    return RedirectResponse("/docs")

@router.get("/app/dashboard", response_class=HTMLResponse)
async def dashboard():
    html = read_template("dashboard.html")
    if html:
        return HTMLResponse(html)
    # Dashboard inline se não tiver template
    return HTMLResponse("""<!DOCTYPE html>
<html lang="pt-BR">
<head><meta charset="UTF-8"><title>Dashboard — EmotionAI</title>
<style>*{margin:0;padding:0;box-sizing:border-box}body{font-family:system-ui;background:#09090B;color:#fff}
.nav{height:64px;background:#18181B;border-bottom:1px solid #3F3F46;display:flex;align-items:center;padding:0 2rem;justify-content:space-between}
.brand{font-size:1.3rem;font-weight:800;text-decoration:none;background:linear-gradient(135deg,#7C3AED,#EC4899);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.container{max-width:1000px;margin:2rem auto;padding:0 2rem}
h1{font-size:2rem;font-weight:800;margin-bottom:0.5rem}
p{color:#A1A1AA;margin-bottom:2rem}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1rem;margin-bottom:2rem}
.stat{background:#1C1C1F;border:1px solid #3F3F46;border-radius:16px;padding:1.5rem;text-align:center}
.stat-num{font-size:2rem;font-weight:900;background:linear-gradient(135deg,#7C3AED,#EC4899);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.stat-label{color:#71717A;font-size:0.8rem;margin-top:0.25rem}
.actions{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1rem}
.action{background:#1C1C1F;border:1px solid #3F3F46;border-radius:16px;padding:1.25rem;text-decoration:none;display:block;transition:border-color 0.2s}
.action:hover{border-color:#7C3AED}
.action-icon{font-size:2rem;margin-bottom:0.5rem}
.action-title{font-weight:700;font-size:0.9rem;color:#FAFAFA}
.action-desc{color:#71717A;font-size:0.8rem;margin-top:0.25rem}
</style>
</head>
<body>
<nav class="nav">
  <a href="/" class="brand">🧠 EmotionAI</a>
  <div id="version" style="color:#71717A;font-size:0.8rem"></div>
</nav>
<div class="container">
  <h1>📊 Dashboard</h1>
  <p>Visão geral da plataforma</p>
  <div class="grid" id="stats">
    <div class="stat"><div class="stat-num" id="s-plugins">...</div><div class="stat-label">Plugins</div></div>
    <div class="stat"><div class="stat-num" id="s-rotas">...</div><div class="stat-label">Rotas</div></div>
    <div class="stat"><div class="stat-num" id="s-ver">...</div><div class="stat-label">Versão</div></div>
    <div class="stat"><div class="stat-num">100%</div><div class="stat-label">Score</div></div>
  </div>
  <div class="actions">
    <a href="/app/avaliacao" class="action"><div class="action-icon">🧪</div><div class="action-title">PHQ-9 + GAD-7</div><div class="action-desc">Escalas clínicas validadas</div></a>
    <a href="/app/chat" class="action"><div class="action-icon">💬</div><div class="action-title">Chat com IA</div><div class="action-desc">Groq + Gemini ativos</div></a>
    <a href="/app/diario" class="action"><div class="action-icon">📔</div><div class="action-title">Diário Emocional</div><div class="action-desc">Registre suas emoções</div></a>
    <a href="/app/planos" class="action"><div class="action-icon">💰</div><div class="action-title">Planos</div><div class="action-desc">Free / Pro / Clínica</div></a>
    <a href="/docs" class="action"><div class="action-icon">📚</div><div class="action-title">API Docs</div><div class="action-desc">1.448+ endpoints</div></a>
    <a href="/api/v1/phq9-clinico/perguntas" class="action"><div class="action-icon">🔬</div><div class="action-title">PHQ-9 API</div><div class="action-desc">Testar endpoint</div></a>
  </div>
</div>
<script>
fetch('/health').then(r=>r.json()).then(d=>{
  document.getElementById('s-plugins').textContent=d.plugins;
  document.getElementById('s-rotas').textContent=d.rotas;
  document.getElementById('s-ver').textContent='v'+d.version;
  document.getElementById('version').textContent='v'+d.version+' · '+d.plugins+' plugins · '+d.rotas+' rotas';
}).catch(()=>{});
</script>
</body>
</html>""")

@router.get("/app/planos", response_class=HTMLResponse)
async def planos():
    html = read_template("planos.html")
    if html:
        return HTMLResponse(html)
    return RedirectResponse("/app/avaliacao")

@router.get("/app/login", response_class=HTMLResponse)
async def login():
    html = read_template("login.html")
    if html:
        return HTMLResponse(html)
    return RedirectResponse("/app/avaliacao")

@router.get("/app/sucesso", response_class=HTMLResponse)
async def sucesso():
    return HTMLResponse("""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>Sucesso</title>
<style>body{font-family:system-ui;background:#09090B;color:#fff;display:flex;align-items:center;justify-content:center;min-height:100vh;text-align:center}
h1{font-size:2rem;margin:1rem 0;background:linear-gradient(135deg,#7C3AED,#EC4899);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
a{display:inline-block;margin-top:1rem;padding:0.75rem 2rem;background:linear-gradient(135deg,#7C3AED,#EC4899);color:white;text-decoration:none;border-radius:10px;font-weight:700}
</style></head>
<body><div><div style="font-size:4rem">🎉</div><h1>Pagamento confirmado!</h1><p style="color:#A1A1AA">Seu plano foi ativado com sucesso.</p><a href="/app/dashboard">Acessar plataforma →</a></div></body>
</html>""")

@router.get("/health")
async def health_ep():
    templates = []
    if os.path.exists("templates"):
        templates = [f for f in os.listdir("templates") if f.endswith(".html")]
    return {
        "status": "ok",
        "templates": templates,
        "templates_count": len(templates),
        "ts": datetime.utcnow().isoformat()
    }

plugin = FrontendRoutesPlugin()
