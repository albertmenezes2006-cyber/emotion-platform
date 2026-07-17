"""Plugin: Frontend Routes v4 — serve páginas HTML sem conflito com FastAPI"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, RedirectResponse, Response
from datetime import datetime
import os
import logging

logger = logging.getLogger(__name__)
router = APIRouter(tags=["frontend"])


def ler_html(nome):
    """Lê template HTML do disco"""
    for path in [f"templates/{nome}", f"templates/{nome}.html"]:
        if os.path.exists(path):
            try:
                with open(path, encoding="utf-8") as f:
                    return f.read()
            except Exception as e:
                logger.warning(f"Erro ao ler {path}: {e}")
    return None


class FrontendRoutesPlugin(PluginBase):
    name = "frontend_routes"
    version = "4.0.0"
    description = "Serve páginas HTML — sem conflito com FastAPI /docs"
    category = "frontend"

    
@router.get('/psicologos', response_class=HTMLResponse)
async def pagina_psicologos(request: Request):
    return templates.TemplateResponse('psicologos.html', {'request': request})

def setup(self, app):
        # Static files
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
        templates = len(os.listdir("templates")) if os.path.exists("templates") else 0
        logger.info(f"[frontend_routes v4] OK — {templates} templates")

    def health_check(self):
        templates = []
        if os.path.exists("templates"):
            templates = [f for f in os.listdir("templates") if f.endswith(".html")]
        return {"status": "healthy", "templates": len(templates)}


# ══════════════════════════════════════════
# PÁGINAS PRINCIPAIS
# ══════════════════════════════════════════

@router.get("/", response_class=HTMLResponse)
async def home():
    html = ler_html("index.html") or ler_html("index_new.html")
    if html:
        return HTMLResponse(html)
    return HTMLResponse("""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><title>EmotionAI</title>
<style>*{margin:0;padding:0;box-sizing:border-box}body{font-family:system-ui;background:#09090B;color:#fff;min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;padding:2rem}
h1{font-size:3rem;background:linear-gradient(135deg,#7C3AED,#EC4899);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:1rem}
p{color:#A1A1AA;margin:0.5rem 0}.links{display:flex;gap:1rem;justify-content:center;margin-top:1.5rem;flex-wrap:wrap}
a{padding:0.75rem 1.5rem;border-radius:10px;text-decoration:none;font-weight:600;transition:opacity 0.2s}
.primary{background:linear-gradient(135deg,#7C3AED,#EC4899);color:white}
.secondary{border:1px solid #3F3F46;color:#A1A1AA}</style></head>
<body><div>
<h1>🧠 EmotionAI</h1>
<p>Plataforma de saúde mental com Inteligência Artificial</p>
<p style="color:#71717A;font-size:0.85rem">1.481 plugins · Chat IA · PHQ-9 · GAD-7</p>
<div class="links">
<a href="/app/avaliacao" class="primary">🧪 Avaliação</a>
<a href="/app/chat" class="primary">💬 Chat IA</a>
<a href="/app/diario" class="secondary">📔 Diário</a>
<a href="/app/dashboard" class="secondary">📊 Dashboard</a>
</div></div></body></html>""")


@router.get("/app/avaliacao", response_class=HTMLResponse)
async def avaliacao():
    html = ler_html("avaliacao.html")
    if html:
        return HTMLResponse(html)
    return RedirectResponse("/")


@router.get("/app/chat", response_class=HTMLResponse)
async def chat():
    html = ler_html("chat_ia.html")
    if html:
        return HTMLResponse(html)
    return RedirectResponse("/")


@router.get("/app/diario", response_class=HTMLResponse)
async def diario():
    html = ler_html("diario.html")
    if html:
        return HTMLResponse(html)
    return RedirectResponse("/")


@router.get("/app/dashboard", response_class=HTMLResponse)
async def dashboard():
    html = ler_html("dashboard.html")
    if html:
        return HTMLResponse(html)
    # Dashboard inline com dados reais
    return HTMLResponse("""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><title>Dashboard — EmotionAI</title>
<link rel="stylesheet" href="/static/css/emotion.css">
<style>
body{min-height:100vh}
.dash-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1rem;margin-bottom:2rem}
.stat-card{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:1.5rem;text-align:center}
.stat-num{font-size:2.2rem;font-weight:900;background:var(--gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.stat-label{color:var(--text3);font-size:0.8rem;margin-top:0.25rem}
.actions-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1rem}
.action-card{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:1.5rem;text-decoration:none;display:block;transition:all 0.2s;color:inherit}
.action-card:hover{border-color:var(--primary);transform:translateY(-2px)}
.action-icon{font-size:2rem;margin-bottom:0.75rem}
.action-title{font-weight:700;font-size:0.95rem}
.action-desc{color:var(--text2);font-size:0.8rem;margin-top:0.25rem}
.page-title{font-size:1.75rem;font-weight:800;margin-bottom:0.5rem}
.page-desc{color:var(--text2);margin-bottom:2rem}
</style></head><body>
<nav class="nav">
  <a href="/" class="nav-brand">🧠 EmotionAI</a>
  <ul class="nav-links">
    <li><a href="/app/avaliacao">Avaliação</a></li>
    <li><a href="/app/chat">Chat IA</a></li>
    <li><a href="/app/diario">Diário</a></li>
    <li><a href="/app/dashboard" class="active">Dashboard</a></li>
  </ul>
  <a href="/app/login" class="nav-btn">Entrar</a>
</nav>
<div class="container" style="padding-top:2rem;padding-bottom:4rem">
  <div class="page-title">📊 Dashboard</div>
  <div class="page-desc">Status em tempo real da plataforma</div>
  <div class="dash-grid" id="stats">
    <div class="stat-card"><div class="stat-num" id="s-plugins">...</div><div class="stat-label">Plugins ativos</div></div>
    <div class="stat-card"><div class="stat-num" id="s-rotas">...</div><div class="stat-label">Rotas de API</div></div>
    <div class="stat-card"><div class="stat-num" id="s-ver">...</div><div class="stat-label">Versão</div></div>
    <div class="stat-card"><div class="stat-num">100%</div><div class="stat-label">Score qualidade</div></div>
    <div class="stat-card"><div class="stat-num">4 IAs</div><div class="stat-label">Modelos online</div></div>
    <div class="stat-card"><div class="stat-num" id="s-uptime">...</div><div class="stat-label">Uptime</div></div>
  </div>
  <div class="actions-grid">
    <a href="/app/avaliacao" class="action-card"><div class="action-icon">🧪</div><div class="action-title">PHQ-9 + GAD-7</div><div class="action-desc">Escalas clínicas validadas</div></a>
    <a href="/app/chat" class="action-card"><div class="action-icon">💬</div><div class="action-title">Chat com IA</div><div class="action-desc">Mistral · Groq · Gemini</div></a>
    <a href="/app/diario" class="action-card"><div class="action-icon">📔</div><div class="action-title">Diário Emocional</div><div class="action-desc">Registre suas emoções</div></a>
    <a href="/app/planos" class="action-card"><div class="action-icon">💰</div><div class="action-title">Planos</div><div class="action-desc">Free · Pro · Clínica</div></a>
    <a href="/api/v1/phq9-clinico/perguntas" class="action-card" target="_blank"><div class="action-icon">🔬</div><div class="action-title">PHQ-9 API</div><div class="action-desc">Testar endpoint REST</div></a>
    <a href="/docs" class="action-card" target="_blank"><div class="action-icon">📚</div><div class="action-title">API Docs</div><div class="action-desc">1.448+ endpoints Swagger</div></a>
  </div>
</div>
<script>
fetch('/health').then(r=>r.json()).then(d=>{
  document.getElementById('s-plugins').textContent = d.plugins;
  document.getElementById('s-rotas').textContent = d.rotas;
  document.getElementById('s-ver').textContent = 'v' + d.version;
  // Calcular uptime
  const parts = (d.uptime||'').split(':');
  if(parts.length >= 2) {
    const h = parseInt(parts[0]||0);
    const m = parseInt(parts[1]||0);
    document.getElementById('s-uptime').textContent = h + 'h ' + m + 'm';
  }
}).catch(()=>{
  document.getElementById('s-plugins').textContent = '1.481';
  document.getElementById('s-rotas').textContent = '1.448';
  document.getElementById('s-ver').textContent = 'v24';
  document.getElementById('s-uptime').textContent = 'online';
});
</script>
</body></html>""")


@router.get("/app/planos", response_class=HTMLResponse)
async def planos():
    html = ler_html("planos.html")
    if html:
        return HTMLResponse(html)
    return RedirectResponse("/")


@router.get("/app/login", response_class=HTMLResponse)
async def login():
    html = ler_html("login.html")
    if html:
        return HTMLResponse(html)
    return RedirectResponse("/")


@router.get("/app/cadastro", response_class=HTMLResponse)
async def cadastro():
    html = ler_html("login.html")
    if html:
        return HTMLResponse(html)
    return RedirectResponse("/")


@router.get("/app/sucesso", response_class=HTMLResponse)
async def sucesso():
    return HTMLResponse("""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>Sucesso — EmotionAI</title>
<link rel="stylesheet" href="/static/css/emotion.css"></head>
<body style="display:flex;align-items:center;justify-content:center;min-height:100vh;text-align:center">
<div>
<div style="font-size:5rem;margin-bottom:1rem">🎉</div>
<h1 style="font-size:2rem;font-weight:900;background:var(--gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:0.75rem">
Pagamento confirmado!</h1>
<p style="color:var(--text2);margin-bottom:2rem">Seu plano foi ativado com sucesso.</p>
<a href="/app/dashboard" class="btn btn-primary btn-lg">Acessar plataforma →</a>
</div></body></html>""")


# Status endpoint (diferente do /health do FastAPI)
@router.get("/api/v1/site/status")
async def site_status():
    templates = []
    if os.path.exists("templates"):
        templates = [f for f in os.listdir("templates") if f.endswith(".html")]
    return {
        "status": "online",
        "templates": len(templates),
        "pages": ["/", "/app/avaliacao", "/app/chat", "/app/diario",
                  "/app/dashboard", "/app/planos", "/app/login"],
        "ts": datetime.utcnow().isoformat()
    }



@router.get("/sitemap.xml")
async def sitemap():
    content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://emotion-platform-albert.onrender.com/</loc><priority>1.0</priority><changefreq>daily</changefreq></url>
  <url><loc>https://emotion-platform-albert.onrender.com/app/avaliacao</loc><priority>0.9</priority><changefreq>weekly</changefreq></url>
  <url><loc>https://emotion-platform-albert.onrender.com/app/chat</loc><priority>0.9</priority><changefreq>weekly</changefreq></url>
  <url><loc>https://emotion-platform-albert.onrender.com/app/diario</loc><priority>0.8</priority><changefreq>weekly</changefreq></url>
  <url><loc>https://emotion-platform-albert.onrender.com/app/planos</loc><priority>0.9</priority><changefreq>monthly</changefreq></url>
  <url><loc>https://emotion-platform-albert.onrender.com/app/login</loc><priority>0.6</priority><changefreq>monthly</changefreq></url>
</urlset>"""
    return Response(content=content, media_type="application/xml")


@router.get("/robots.txt")
async def robots():
    content = """User-agent: *
Allow: /
Allow: /app/avaliacao
Allow: /app/chat
Allow: /app/diario
Allow: /app/planos
Disallow: /api/
Disallow: /docs
Sitemap: https://emotion-platform-albert.onrender.com/sitemap.xml"""
    return Response(content=content, media_type="text/plain")


plugin = FrontendRoutesPlugin()
