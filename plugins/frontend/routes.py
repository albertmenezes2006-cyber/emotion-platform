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
    """Le template HTML do disco"""
    for path in [f"templates/{nome}", f"templates/{nome}.html"]:
        if os.path.exists(path):
            try:
                with open(path, encoding="utf-8") as f:
                    return f.read()
            except Exception as e:
                logger.warning(f"Erro ao ler {path}: {e}")
    return None


# ══════════════════════════════════════════
# PAGINAS PRINCIPAIS
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
<h1>Emotion Intelligence Platform</h1>
<p>Plataforma de saude mental com Inteligencia Artificial</p>
<div class="links">
<a href="/app/avaliacao" class="primary">Avaliacao PHQ-9</a>
<a href="/app/chat" class="primary">Chat IA</a>
<a href="/psicologos" class="primary">Para Psicologos</a>
<a href="/app/diario" class="secondary">Diario</a>
<a href="/app/dashboard" class="secondary">Dashboard</a>
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
    return RedirectResponse("/")


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
<html><head><meta charset="UTF-8"><title>Sucesso</title></head>
<body style="font-family:system-ui;background:#0f172a;color:#e2e8f0;display:flex;align-items:center;justify-content:center;min-height:100vh;text-align:center">
<div>
<div style="font-size:5rem">🎉</div>
<h1 style="color:#7c3aed;margin:20px 0">Pagamento confirmado!</h1>
<p style="color:#64748b;margin-bottom:32px">Seu plano foi ativado com sucesso.</p>
<a href="/app/dashboard" style="background:#7c3aed;color:white;padding:14px 28px;border-radius:10px;text-decoration:none;font-weight:700">Acessar plataforma</a>
</div></body></html>""")


@router.get("/psicologos", response_class=HTMLResponse)
async def psicologos():
    html = ler_html("psicologos.html")
    if html:
        return HTMLResponse(html)
    return HTMLResponse("<h1>Pagina psicologos.html nao encontrada</h1>", status_code=404)


@router.get("/api/v1/site/status")
async def site_status():
    templates = []
    if os.path.exists("templates"):
        templates = [f for f in os.listdir("templates") if f.endswith(".html")]
    return {
        "status": "online",
        "templates": len(templates),
        "pages": ["/", "/app/avaliacao", "/app/chat", "/app/diario",
                  "/app/dashboard", "/app/planos", "/app/login", "/psicologos"],
        "ts": datetime.utcnow().isoformat()
    }


@router.get("/sitemap.xml")
async def sitemap():
    BASE = os.getenv("BASE_URL", "https://emotion-platform-albert.onrender.com")
    content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>{BASE}/</loc><priority>1.0</priority><changefreq>daily</changefreq></url>
  <url><loc>{BASE}/psicologos</loc><priority>0.95</priority><changefreq>weekly</changefreq></url>
  <url><loc>{BASE}/app/avaliacao</loc><priority>0.9</priority><changefreq>weekly</changefreq></url>
  <url><loc>{BASE}/app/chat</loc><priority>0.9</priority><changefreq>weekly</changefreq></url>
  <url><loc>{BASE}/app/diario</loc><priority>0.8</priority><changefreq>weekly</changefreq></url>
  <url><loc>{BASE}/app/planos</loc><priority>0.9</priority><changefreq>monthly</changefreq></url>
  <url><loc>{BASE}/app/login</loc><priority>0.6</priority><changefreq>monthly</changefreq></url>
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
Allow: /psicologos
Disallow: /api/
Disallow: /admin/
Sitemap: https://emotion-platform-albert.onrender.com/sitemap.xml"""
    return Response(content=content, media_type="text/plain")


class FrontendRoutesPlugin(PluginBase):
    name = "frontend_routes"
    version = "4.1.0"
    description = "Serve paginas HTML"
    category = "frontend"

    def setup(self, app):
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
        logger.info(f"[frontend_routes v4.1] OK — {templates} templates")

    def health_check(self):
        templates = []
        if os.path.exists("templates"):
            templates = [f for f in os.listdir("templates") if f.endswith(".html")]
        return {"status": "healthy", "templates": len(templates)}


plugin = FrontendRoutesPlugin()


# ══════════════════════════════════════
# ROTAS PARA TEMPLATES ORFAOS
# ══════════════════════════════════════

@router.get("/app/analises", response_class=HTMLResponse)
async def page_analises():
    html = ler_html("analises.html")
    if html:
        return HTMLResponse(html)
    return HTMLResponse("<h1>analises</h1><p>Página em construção</p>", status_code=200)

@router.get("/api-docs", response_class=HTMLResponse)
async def page_api_docs():
    html = ler_html("api_docs.html")
    if html:
        return HTMLResponse(html)
    return HTMLResponse("<h1>api_docs</h1><p>Página em construção</p>", status_code=200)

@router.get("/app/carteira", response_class=HTMLResponse)
async def page_carteira():
    html = ler_html("carteira.html")
    if html:
        return HTMLResponse(html)
    return HTMLResponse("<h1>carteira</h1><p>Página em construção</p>", status_code=200)

@router.get("/checkout/anual", response_class=HTMLResponse)
async def page_checkout_anual():
    html = ler_html("checkout_anual.html")
    if html:
        return HTMLResponse(html)
    return HTMLResponse("<h1>checkout_anual</h1><p>Página em construção</p>", status_code=200)

@router.get("/checkout/api", response_class=HTMLResponse)
async def page_checkout_api():
    html = ler_html("checkout_api.html")
    if html:
        return HTMLResponse(html)
    return HTMLResponse("<h1>checkout_api</h1><p>Página em construção</p>", status_code=200)

@router.get("/checkout/creditos", response_class=HTMLResponse)
async def page_checkout_creditos():
    html = ler_html("checkout_creditos.html")
    if html:
        return HTMLResponse(html)
    return HTMLResponse("<h1>checkout_creditos</h1><p>Página em construção</p>", status_code=200)

@router.get("/checkout/relatorio", response_class=HTMLResponse)
async def page_checkout_relatorio():
    html = ler_html("checkout_relatorio.html")
    if html:
        return HTMLResponse(html)
    return HTMLResponse("<h1>checkout_relatorio</h1><p>Página em construção</p>", status_code=200)

@router.get("/checkout/sofia", response_class=HTMLResponse)
async def page_checkout_sofia():
    html = ler_html("checkout_sofia.html")
    if html:
        return HTMLResponse(html)
    return HTMLResponse("<h1>checkout_sofia</h1><p>Página em construção</p>", status_code=200)

@router.get("/nova-senha", response_class=HTMLResponse)
async def page_nova_senha():
    html = ler_html("nova_senha.html")
    if html:
        return HTMLResponse(html)
    return HTMLResponse("<h1>nova_senha</h1><p>Página em construção</p>", status_code=200)

@router.get("/premium", response_class=HTMLResponse)
async def page_premium():
    html = ler_html("premium.html")
    if html:
        return HTMLResponse(html)
    return HTMLResponse("<h1>premium</h1><p>Página em construção</p>", status_code=200)

@router.get("/presente/sucesso", response_class=HTMLResponse)
async def page_presente_sucesso():
    html = ler_html("presente_sucesso.html")
    if html:
        return HTMLResponse(html)
    return HTMLResponse("<h1>presente_sucesso</h1><p>Página em construção</p>", status_code=200)

@router.get("/app/score-ie", response_class=HTMLResponse)
async def page_score_ie():
    html = ler_html("score_ie.html")
    if html:
        return HTMLResponse(html)
    return HTMLResponse("<h1>score_ie</h1><p>Página em construção</p>", status_code=200)

@router.get("/whitelabel", response_class=HTMLResponse)
async def page_whitelabel():
    html = ler_html("whitelabel.html")
    if html:
        return HTMLResponse(html)
    return HTMLResponse("<h1>whitelabel</h1><p>Página em construção</p>", status_code=200)

@router.get("/afiliado", response_class=HTMLResponse)
async def page_afiliado():
    html = ler_html("afiliado.html")
    return HTMLResponse(html) if html else HTMLResponse("<h1>Afiliados</h1>")

@router.get("/manifest.json")
async def manifest_json():
    import json as _json
    from fastapi.responses import JSONResponse
    try:
        data = _json.loads(open("static/manifest.json", encoding="utf-8").read())
        return JSONResponse(data, headers={"Content-Type": "application/manifest+json"})
    except Exception:
        return JSONResponse({"name": "EmotionAI", "start_url": "/"})

@router.get("/sw.js")
async def service_worker():
    from fastapi.responses import Response
    try:
        sw = open("static/sw.js", encoding="utf-8").read()
        return Response(sw, media_type="application/javascript")
    except Exception:
        return Response("// sw", media_type="application/javascript")

# Rotas templates orfaos

@router.get("/faq", response_class=HTMLResponse)
async def page_faq():
    html = ler_html("faq.html")
    return HTMLResponse(html) if html else HTMLResponse("<h1>faq</h1>")

@router.get("/recuperar-senha", response_class=HTMLResponse)
async def page_recuperar_senha():
    html = ler_html("recuperar_senha.html")
    return HTMLResponse(html) if html else HTMLResponse("<h1>recuperar_senha</h1>")

@router.get("/blog/artigo", response_class=HTMLResponse)
async def page_artigo():
    html = ler_html("artigo.html")
    return HTMLResponse(html) if html else HTMLResponse("<h1>artigo</h1>")

@router.get("/compartilhar", response_class=HTMLResponse)
async def page_compartilhar():
    html = ler_html("compartilhar.html")
    return HTMLResponse(html) if html else HTMLResponse("<h1>compartilhar</h1>")

@router.get("/sobre", response_class=HTMLResponse)
async def page_sobre():
    html = ler_html("sobre.html")
    return HTMLResponse(html) if html else HTMLResponse("<h1>sobre</h1>")

@router.get("/app/gamificacao", response_class=HTMLResponse)
async def page_gamificacao():
    html = ler_html("gamificacao.html")
    return HTMLResponse(html) if html else HTMLResponse("<h1>gamificacao</h1>")

@router.get("/privacidade", response_class=HTMLResponse)
async def page_privacidade():
    html = ler_html("privacidade.html")
    return HTMLResponse(html) if html else HTMLResponse("<h1>privacidade</h1>")

@router.get("/erro-500", response_class=HTMLResponse)
async def page_500():
    html = ler_html("500.html")
    return HTMLResponse(html) if html else HTMLResponse("<h1>500</h1>")

@router.get("/offline", response_class=HTMLResponse)
async def page_offline():
    html = ler_html("offline.html")
    return HTMLResponse(html) if html else HTMLResponse("<h1>offline</h1>")

@router.get("/app/perfil", response_class=HTMLResponse)
async def page_perfil():
    html = ler_html("perfil.html")
    return HTMLResponse(html) if html else HTMLResponse("<h1>perfil</h1>")

@router.get("/obrigado", response_class=HTMLResponse)
async def page_obrigado():
    html = ler_html("obrigado.html")
    return HTMLResponse(html) if html else HTMLResponse("<h1>obrigado</h1>")

@router.get("/blog", response_class=HTMLResponse)
async def page_blog():
    html = ler_html("blog.html")
    return HTMLResponse(html) if html else HTMLResponse("<h1>blog</h1>")

@router.get("/app/configuracoes", response_class=HTMLResponse)
async def page_configuracoes():
    html = ler_html("configuracoes.html")
    return HTMLResponse(html) if html else HTMLResponse("<h1>configuracoes</h1>")

@router.get("/app/ranking", response_class=HTMLResponse)
async def page_ranking():
    html = ler_html("ranking.html")
    return HTMLResponse(html) if html else HTMLResponse("<h1>ranking</h1>")

@router.get("/contato", response_class=HTMLResponse)
async def page_contato():
    html = ler_html("contato.html")
    return HTMLResponse(html) if html else HTMLResponse("<h1>contato</h1>")

@router.get("/terapia", response_class=HTMLResponse)
async def page_terapia():
    html = ler_html("terapia.html")
    return HTMLResponse(html) if html else HTMLResponse("<h1>terapia</h1>")

@router.get("/termos", response_class=HTMLResponse)
async def page_termos():
    html = ler_html("termos.html")
    return HTMLResponse(html) if html else HTMLResponse("<h1>termos</h1>")

@router.get("/planos", response_class=HTMLResponse)
async def page_planos_root():
    html = ler_html("planos.html")
    return HTMLResponse(html) if html else HTMLResponse("<h1>Planos</h1>")

@router.get("/checkout", response_class=HTMLResponse)
async def page_checkout_root():
    html = ler_html("checkout.html")
    return HTMLResponse(html) if html else HTMLResponse("<h1>Checkout</h1>")

@router.get("/blog/phq9-guia", response_class=HTMLResponse)
async def artigo_phq9():
    html = ler_html("artigo_phq9.html")
    return HTMLResponse(html) if html else HTMLResponse("<h1>PHQ-9</h1>")

@router.get("/blog/gad7-guia", response_class=HTMLResponse)
async def artigo_gad7():
    html = ler_html("artigo_gad7.html")
    return HTMLResponse(html) if html else HTMLResponse("<h1>GAD-7</h1>")

@router.get("/blog/telepsicologia", response_class=HTMLResponse)
async def artigo_tele():
    html = ler_html("artigo_tele.html")
    return HTMLResponse(html) if html else HTMLResponse("<h1>Telepsicologia</h1>")

@router.get("/comparativo", response_class=HTMLResponse)
async def page_comparativo():
    html = ler_html("comparativo.html")
    return HTMLResponse(html) if html else HTMLResponse("<h1>Comparativo</h1>")

@router.get("/para-clinicas", response_class=HTMLResponse)
async def page_clinicas():
    html = ler_html("para-clinicas.html")
    return HTMLResponse(html) if html else HTMLResponse("<h1>Para Clínicas</h1>")
