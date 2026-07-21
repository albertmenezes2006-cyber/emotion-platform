"""
Plugin: QR Code - gera QR codes para o site
Albert Menezes - Emotion Intelligence Platform
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
import os, logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/qr", tags=["QR Code"])
BASE   = os.getenv("BASE_URL", "https://emotion-platform-albert.onrender.com")

CSS = """
<style>
body{font-family:system-ui;background:#0f172a;color:#e2e8f0;
     display:flex;align-items:center;justify-content:center;
     min-height:100vh;flex-direction:column;gap:24px;padding:20px;}
.card{background:white;border-radius:16px;padding:32px;text-align:center;max-width:320px;}
img{width:256px;height:256px;}
h1{color:#7c3aed;margin-bottom:8px;font-size:20px;}
p{color:#64748b;font-size:14px;}
.url{color:#7c3aed;font-family:monospace;font-size:11px;margin-top:8px;word-break:break-all;}
.btns{display:flex;gap:12px;flex-wrap:wrap;justify-content:center;}
a.btn{padding:10px 20px;background:#7c3aed;color:white;border-radius:8px;text-decoration:none;font-size:14px;}
a.btn2{padding:10px 20px;background:#1e293b;color:#a78bfa;border:1px solid #7c3aed;border-radius:8px;text-decoration:none;font-size:14px;}
</style>
"""

def _page(titulo, url, desc):
    qr = "https://api.qrserver.com/v1/create-qr-code/?size=256x256&color=7c3aed&bgcolor=ffffff&data=" + url
    html = (
        "<!DOCTYPE html><html lang='pt-BR'><head><meta charset='UTF-8'>"
        "<meta name='robots' content='noindex'>"
        "<title>QR - " + titulo + "</title>" + CSS + "</head><body>"
        "<div class='card'>"
        "<h1>" + titulo + "</h1>"
        "<img src='" + qr + "' alt='QR Code'>"
        "<p>" + desc + "</p>"
        "<p class='url'>" + url + "</p>"
        "</div>"
        "<div class='btns'>"
        "<a class='btn' href='" + url + "'>Acessar</a>"
        "<a class='btn2' href='" + qr + "' download='qrcode.png'>Baixar PNG</a>"
        "<a class='btn2' href='/qr/'>Todos QRs</a>"
        "</div></body></html>"
    )
    return HTMLResponse(html)


@router.get("/", response_class=HTMLResponse)
async def qr_home():
    links = [
        ("/qr/site",      "Site Principal",   BASE),
        ("/qr/avaliacao", "PHQ-9 e GAD-7",    BASE + "/app/avaliacao"),
        ("/qr/chat",      "Chat com IA",      BASE + "/app/chat"),
        ("/qr/planos",    "Planos e Precos",  BASE + "/app/planos"),
        ("/qr/admin",     "Painel Admin",     BASE + "/admin/"),
    ]
    itens = ""
    for link, nome, url in links:
        itens += (
            "<a href='" + link + "' style='display:block;padding:14px;"
            "background:#1e293b;border-radius:8px;color:#a78bfa;"
            "text-decoration:none;margin-bottom:8px;font-size:14px;'>"
            + nome + "<br><small style='color:#475569;font-size:11px;'>" + url + "</small></a>"
        )
    html = (
        "<!DOCTYPE html><html lang='pt-BR'><head><meta charset='UTF-8'>"
        "<meta name='robots' content='noindex'><title>QR Codes</title>"
        "<style>body{font-family:system-ui;background:#0f172a;color:#e2e8f0;padding:40px 20px;}"
        ".c{max-width:600px;margin:0 auto;}"
        "h1{color:#7c3aed;margin-bottom:8px;}p{color:#64748b;margin-bottom:24px;}</style>"
        "</head><body><div class='c'>"
        "<h1>QR Codes - Emotion Platform</h1>"
        "<p>Escolha qual QR Code voce quer gerar:</p>"
        + itens +
        "</div></body></html>"
    )
    return HTMLResponse(html)


@router.get("/site", response_class=HTMLResponse)
async def qr_site():
    return _page("Site Principal", BASE, "Escaneie para acessar a plataforma")

@router.get("/avaliacao", response_class=HTMLResponse)
async def qr_avaliacao():
    return _page("Avaliacao PHQ-9 e GAD-7", BASE + "/app/avaliacao", "Escaneie para fazer a avaliacao")

@router.get("/chat", response_class=HTMLResponse)
async def qr_chat():
    return _page("Chat com IA", BASE + "/app/chat", "Escaneie para conversar com a IA")

@router.get("/planos", response_class=HTMLResponse)
async def qr_planos():
    return _page("Planos e Precos", BASE + "/app/planos", "Escaneie para ver os planos")

@router.get("/admin", response_class=HTMLResponse)
async def qr_admin():
    return _page("Painel Admin", BASE + "/admin/", "Escaneie para acessar o painel admin")

@router.get("/status")
async def qr_status():
    return {
        "status":   "online",
        "qrcodes":  ["/qr/site", "/qr/avaliacao", "/qr/chat", "/qr/planos", "/qr/admin"],
        "base_url": BASE,
        "api_qr":   "https://api.qrserver.com"
    }


class QRCodePlugin(PluginBase):
    name        = "qrcode_plugin"
    version     = "1.0.0"
    description = "QR Codes para site avaliacao chat e planos"
    category    = "utilidades"

    def setup(self, app):
        app.include_router(router)
        logger.info("[QR] OK")

    def health_check(self):
        return {"status": "healthy", "plugin": self.name}


plugin = QRCodePlugin()
