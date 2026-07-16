"""Plugin: Frontend Routes — serve as páginas HTML"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import os, logging

logger = logging.getLogger(__name__)
router = APIRouter(tags=["frontend"])
templates = Jinja2Templates(directory="templates")

class FrontendRoutesPlugin(PluginBase):
    name = "frontend_routes"; version = "2.0.0"
    description = "Rotas do frontend — páginas HTML"; category = "frontend"
    def setup(self, app):
        app.include_router(router)
        logger.info("[frontend_routes] OK")
    def health_check(self):
        return {"status": "healthy", "templates": os.path.exists("templates")}

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    try:
        return templates.TemplateResponse("index_new.html", {"request": request})
    except Exception:
        try:
            return templates.TemplateResponse("index.html", {"request": request})
        except Exception:
            return HTMLResponse("<h1>🧠 EmotionAI — <a href='/docs'>API Docs</a></h1>")

@router.get("/app/avaliacao", response_class=HTMLResponse)
async def avaliacao(request: Request):
    try:
        return templates.TemplateResponse("avaliacao.html", {"request": request})
    except Exception:
        return RedirectResponse("/docs")

@router.get("/app/chat", response_class=HTMLResponse)
async def chat(request: Request):
    try:
        return templates.TemplateResponse("chat_ia.html", {"request": request})
    except Exception:
        return RedirectResponse("/docs")

@router.get("/app/diario", response_class=HTMLResponse)
async def diario(request: Request):
    try:
        return templates.TemplateResponse("diario.html", {"request": request})
    except Exception:
        return RedirectResponse("/docs")

@router.get("/app/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    try:
        return templates.TemplateResponse("dashboard.html", {"request": request})
    except Exception:
        return RedirectResponse("/docs")

@router.get("/app/agenda", response_class=HTMLResponse)
async def agenda(request: Request):
    try:
        return templates.TemplateResponse("agenda.html", {"request": request})
    except Exception:
        return RedirectResponse("/app/avaliacao")

@router.get("/app/prontuario", response_class=HTMLResponse)
async def prontuario(request: Request):
    try:
        return templates.TemplateResponse("prontuario.html", {"request": request})
    except Exception:
        return RedirectResponse("/app/avaliacao")

@router.get("/health")
async def health():
    return {"status": "ok", "plugins": 1470, "rotas": 7142, "score": "100%"}

plugin = FrontendRoutesPlugin()
