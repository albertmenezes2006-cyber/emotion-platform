"""Plugin: Buy Me a Coffee + Ko-fi + Patreon"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, RedirectResponse
import os, logging

logger       = logging.getLogger(__name__)
router       = APIRouter(prefix="/api/v1/tip", tags=["Monetizacao"])
BMC_USER     = os.getenv("BMC_USERNAME", "")
KOFI_USER    = os.getenv("KOFI_USERNAME", "")
PATREON_USER = os.getenv("PATREON_USERNAME", "")
BASE         = os.getenv("BASE_URL", "https://emotion-platform-albert.onrender.com")

@router.get("/status")
async def status():
    return {
        "buymeacoffee": {
            "configurado": bool(BMC_USER),
            "url": "https://buymeacoffee.com/" + BMC_USER if BMC_USER else "configurar BMC_USERNAME",
            "taxa": "5%", "aprovacao": "Instantanea",
            "como": "buymeacoffee.com -> criar conta -> Render: BMC_USERNAME=seuuser"
        },
        "kofi": {
            "configurado": bool(KOFI_USER),
            "url": "https://ko-fi.com/" + KOFI_USER if KOFI_USER else "configurar KOFI_USERNAME",
            "taxa": "0% gratis", "aprovacao": "Instantanea",
            "como": "ko-fi.com -> criar conta -> Render: KOFI_USERNAME=seuuser"
        },
        "patreon": {
            "configurado": bool(PATREON_USER),
            "url": "https://patreon.com/" + PATREON_USER if PATREON_USER else "configurar PATREON_USERNAME",
            "taxa": "8-12%", "aprovacao": "Instantanea",
            "como": "patreon.com/create -> Render: PATREON_USERNAME=seuuser"
        }
    }

@router.get("/apoiar", response_class=HTMLResponse)
async def pagina_apoio():
    bmc     = "https://buymeacoffee.com/" + BMC_USER if BMC_USER else "https://buymeacoffee.com"
    kofi    = "https://ko-fi.com/" + KOFI_USER if KOFI_USER else "https://ko-fi.com"
    patreon = "https://patreon.com/" + PATREON_USER if PATREON_USER else "https://patreon.com"
    doacao  = BASE + "/api/v1/doacao/page"
    planos  = BASE + "/app/planos"

    return HTMLResponse(
        "<!DOCTYPE html>"
        "<html lang='pt-BR'><head><meta charset='UTF-8'>"
        "<title>Apoiar - Emotion Platform</title>"
        "<style>"
        "body{font-family:system-ui;background:#0f172a;color:#e2e8f0;"
        "display:flex;align-items:center;justify-content:center;min-height:100vh;padding:20px;}"
        ".c{max-width:700px;width:100%;text-align:center;}"
        "h1{color:#7c3aed;font-size:32px;}"
        ".sub{color:#64748b;margin-bottom:40px;}"
        ".grid{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;margin:30px 0;}"
        ".card{background:#1e293b;border-radius:16px;padding:30px;"
        "border:2px solid #334155;text-decoration:none;color:white;"
        "transition:all .2s;display:block;}"
        ".card:hover{border-color:#7c3aed;transform:translateY(-4px);}"
        ".emoji{font-size:48px;margin-bottom:12px;}"
        ".card h3{color:#a78bfa;margin-bottom:8px;}"
        ".card p{color:#64748b;font-size:13px;margin:0;}"
        ".badge{background:#064e3b;color:#34d399;padding:4px 10px;"
        "border-radius:20px;font-size:11px;margin-top:8px;display:inline-block;}"
        ".bb{background:#1e3a5f;color:#60a5fa;}"
        ".ft{font-size:13px;color:#475569;margin-top:20px;}"
        ".ft a{color:#7c3aed;}"
        "</style></head><body><div class='c'>"
        "<div style='font-size:64px'>💜</div>"
        "<h1>Apoiar o Emotion Platform</h1>"
        "<p class='sub'>Sua contribuicao mantem a plataforma gratuita!</p>"
        "<div class='grid'>"
        "<a class='card' href='" + bmc + "' target='_blank'>"
        "<div class='emoji'>☕</div><h3>Buy Me a Coffee</h3>"
        "<p>Doacao unica ou mensal. Simples!</p>"
        "<span class='badge'>Mais popular</span></a>"
        "<a class='card' href='" + kofi + "' target='_blank'>"
        "<div class='emoji'>🎨</div><h3>Ko-fi</h3>"
        "<p>Zero taxa! Todo dinheiro vai ao projeto.</p>"
        "<span class='badge'>0% taxa</span></a>"
        "<a class='card' href='" + patreon + "' target='_blank'>"
        "<div class='emoji'>🎯</div><h3>Patreon</h3>"
        "<p>Apoiador mensal com beneficios!</p>"
        "<span class='badge bb'>Beneficios</span></a>"
        "<a class='card' href='" + doacao + "'>"
        "<div class='emoji'>💳</div><h3>Doacao Direta</h3>"
        "<p>Cartao de credito via Stripe. R$ 5-100.</p>"
        "<span class='badge bb'>Stripe</span></a>"
        "</div>"
        "<p class='ft'>Prefere acesso completo? "
        "<a href='" + planos + "'>Ver planos Pro e Clinica</a></p>"
        "</div></body></html>"
    )

@router.get("/bmc")
async def ir_bmc():
    return RedirectResponse("https://buymeacoffee.com/" + BMC_USER if BMC_USER else "https://buymeacoffee.com")

@router.get("/kofi")
async def ir_kofi():
    return RedirectResponse("https://ko-fi.com/" + KOFI_USER if KOFI_USER else "https://ko-fi.com")

@router.get("/patreon")
async def ir_patreon():
    return RedirectResponse("https://patreon.com/" + PATREON_USER if PATREON_USER else "https://patreon.com")

class TipExternoPlugin(PluginBase):
    name = "tip_externo"
    version = "1.0.1"
    description = "Buy Me a Coffee + Ko-fi + Patreon"
    category = "monetizacao_real"
    def setup(self, app):
        app.include_router(router)
        logger.info("[TipExterno] OK")
    def health_check(self):
        return {"status": "healthy", "bmc": bool(BMC_USER), "kofi": bool(KOFI_USER)}

plugin = TipExternoPlugin()
