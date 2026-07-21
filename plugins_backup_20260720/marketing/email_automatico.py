#!/usr/bin/env python3
"""Email automático — boas-vindas e nurture"""
from fastapi import APIRouter, BackgroundTasks
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
import httpx
import os
from datetime import datetime

router = APIRouter(prefix="/api/v1/email", tags=["Email"])

BREVO_API_KEY = os.getenv("BREVO_API_KEY", "")
FROM_EMAIL = "albertmenezes2006@gmail.com"
FROM_NAME = "Albert — Emotion Platform"

async def enviar_email_brevo(
    para: str,
    nome: str,
    assunto: str,
    html: str
):
    """Envia email via Brevo (300/dia grátis)"""
    if not BREVO_API_KEY:
        print(f"📧 [SIMULADO] Email para {para}: {assunto}")
        return True
    
    async with httpx.AsyncClient() as client:
        r = await client.post(
            "https://api.brevo.com/v3/smtp/email",
            headers={
                "api-key": BREVO_API_KEY,
                "Content-Type": "application/json"
            },
            json={
                "sender": {"name": FROM_NAME, "email": FROM_EMAIL},
                "to": [{"email": para, "name": nome}],
                "subject": assunto,
                "htmlContent": html
            },
            timeout=10
        )
        return r.status_code == 201

def html_boas_vindas(nome: str) -> str:
    return f"""
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"></head>
<body style="font-family:sans-serif;max-width:600px;margin:0 auto;padding:20px">
    <div style="background:linear-gradient(135deg,#667eea,#764ba2);
                border-radius:16px;padding:40px;text-align:center;color:white">
        <h1 style="margin:0;font-size:28px">🧠 Bem-vindo ao Emotion Platform!</h1>
        <p style="opacity:0.9;margin-top:8px">A plataforma #1 de saúde mental com IA no Brasil</p>
    </div>
    
    <div style="padding:32px 0">
        <p style="font-size:18px;color:#333">Olá, <strong>{nome}</strong>! 👋</p>
        
        <p style="color:#666;line-height:1.6">
            Ficamos felizes em ter você conosco. 
            Sua conta está pronta para usar.
        </p>
        
        <h2 style="color:#333">O que você pode fazer agora:</h2>
        
        <div style="background:#f8f9fa;border-radius:12px;padding:20px;margin:16px 0">
            <p>✅ <strong>Aplicar PHQ-9 e GAD-7</strong> — avaliações validadas</p>
            <p>✅ <strong>Chat com IA</strong> — suporte 24h em português</p>
            <p>✅ <strong>Diário emocional</strong> — acompanhar evolução</p>
            <p>✅ <strong>Prontuário digital</strong> — gestão completa</p>
        </div>
        
        <div style="text-align:center;margin:32px 0">
            <a href="https://emotion-platform-albert.onrender.com"
               style="background:linear-gradient(135deg,#667eea,#764ba2);
                      color:white;padding:16px 32px;border-radius:12px;
                      text-decoration:none;font-weight:700;font-size:16px">
                🚀 Acessar Plataforma
            </a>
        </div>
        
        <p style="color:#888;font-size:14px">
            Qualquer dúvida, responda este email.<br>
            — Albert, fundador do Emotion Platform
        </p>
    </div>
    
    <div style="border-top:1px solid #eee;padding-top:16px;
                color:#aaa;font-size:12px;text-align:center">
        Emotion Intelligence Platform — Saúde mental com IA<br>
        <a href="#" style="color:#aaa">Cancelar inscrição</a>
    </div>
</body>
</html>"""

@router.post("/boas-vindas")
async def email_boas_vindas(
    email: str,
    nome: str,
    background: BackgroundTasks
):
    background.add_task(
        enviar_email_brevo,
        email, nome,
        f"🧠 Bem-vindo ao Emotion Platform, {nome}!",
        html_boas_vindas(nome)
    )
    return JSONResponse({"ok": True, "msg": "Email enviado"})

@router.get("/status")
async def status_email():
    return {
        "brevo_configurado": bool(BREVO_API_KEY),
        "from": FROM_EMAIL,
        "limite_diario": "300 emails grátis",
        "status": "ativo" if BREVO_API_KEY else "configurar BREVO_API_KEY"
    }

class EmailPlugin(PluginBase):
    name = "email_automatico"
    def setup(self, app):
        app.include_router(router)

plugin = EmailPlugin()
