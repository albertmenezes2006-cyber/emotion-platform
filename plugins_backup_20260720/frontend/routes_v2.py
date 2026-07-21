"""Plugin: Frontend Routes V2 — planos, login, cadastro, mobile"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import logging

logger = logging.getLogger(__name__)
router = APIRouter(tags=["frontend_v2"])
templates = Jinja2Templates(directory="templates")

class FrontendRoutesV2Plugin(PluginBase):
    name = "frontend_routes_v2"; version = "2.0.0"
    description = "Rotas v2 — planos, login, mobile"; category = "frontend"
    def setup(self, app):
        app.include_router(router)
        logger.info("[frontend_routes_v2] OK")
    def health_check(self): return {"status": "healthy"}

@router.get("/app/planos", response_class=HTMLResponse)
async def planos(request: Request):
    try: return templates.TemplateResponse("planos.html", {"request": request})
    except Exception: return RedirectResponse("/app/avaliacao")

@router.get("/app/login", response_class=HTMLResponse)
async def login(request: Request):
    try: return templates.TemplateResponse("login.html", {"request": request})
    except Exception: return RedirectResponse("/docs")

@router.get("/app/cadastro", response_class=HTMLResponse)
async def cadastro(request: Request):
    try: return templates.TemplateResponse("login.html", {"request": request})
    except Exception: return RedirectResponse("/docs")

@router.get("/app/sucesso", response_class=HTMLResponse)
async def sucesso(request: Request):
    return HTMLResponse("""
    <html><head><link rel="stylesheet" href="/static/css/emotion.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@700;900&display=swap" rel="stylesheet">
    </head><body style="display:flex;align-items:center;justify-content:center;min-height:100vh;text-align:center">
    <div>
      <div style="font-size:5rem">🎉</div>
      <h1 style="font-size:2rem;background:linear-gradient(135deg,#6C63FF,#FF6584);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin:1rem 0">
        Pagamento confirmado!</h1>
      <p style="color:#A7A9BE;margin-bottom:2rem">Seu plano foi ativado com sucesso.</p>
      <a href="/app/dashboard" style="background:linear-gradient(135deg,#6C63FF,#FF6584);color:white;padding:1rem 2rem;border-radius:12px;text-decoration:none;font-weight:700">
        Acessar plataforma →</a>
    </div></body></html>
    """)

@router.get("/app/mobile-sdk")
async def mobile_sdk_info():
    return {
        "sdk": "Emotion Intelligence Platform SDK",
        "versao": "2.0.0",
        "docs": "https://emotion-platform-albert.onrender.com/docs",
        "config_endpoint": "https://emotion-platform-albert.onrender.com/api/mobile/v1/sdk/config",
        "react_native": {
            "install": "npm install @emotion-ai/react-native-sdk",
            "exemplo": "import { EmotionAI } from '@emotion-ai/react-native-sdk';"
        },
        "flutter": {
            "install": "emotion_ai_flutter: ^2.0.0",
            "exemplo": "import 'package:emotion_ai_flutter/emotion_ai.dart';"
        }
    }

plugin = FrontendRoutesV2Plugin()
