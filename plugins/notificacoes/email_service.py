"""Servico de email via Brevo HTTP (funciona no Render)"""
import os
import logging
import httpx

logger = logging.getLogger(__name__)

BREVO_KEY = os.getenv("BREVO_API_KEY", "")
FROM_EMAIL = os.getenv("FROM_EMAIL", "albertmenezes2006@gmail.com")
FROM_NAME = os.getenv("FROM_NAME", "EmotionAI")


def enviar_email(destinatario: str, assunto: str, html: str, nome: str = "") -> bool:
    if not BREVO_KEY:
        logger.warning("BREVO_API_KEY nao configurado")
        return False
    try:
        r = httpx.post(
            "https://api.brevo.com/v3/smtp/email",
            headers={"api-key": BREVO_KEY, "Content-Type": "application/json"},
            json={
                "sender": {"name": FROM_NAME, "email": FROM_EMAIL},
                "to": [{"email": destinatario, "name": nome or destinatario}],
                "subject": assunto,
                "htmlContent": html
            },
            timeout=10
        )
        if r.status_code in (200, 201):
            return True
        logger.error(f"Brevo erro {r.status_code}: {r.text}")
        return False
    except Exception as e:
        logger.error(f"Erro envio: {e}")
        return False


def email_pagamento_aprovado(destinatario, plano, valor, payment_id):
    plano_nome = "Pro" if plano == "pro" else "Clinica" if plano == "clinica" else plano.title()
    html = f"""<div style="font-family:sans-serif;max-width:560px;margin:auto;padding:30px;background:#fff;border-radius:12px;box-shadow:0 4px 20px rgba(0,0,0,0.08)">
    <div style="text-align:center;margin-bottom:20px">
      <div style="width:70px;height:70px;background:linear-gradient(135deg,#10b981,#059669);border-radius:50%;display:inline-block;line-height:70px;color:white;font-size:36px">check</div>
    </div>
    <h1 style="color:#1e293b;text-align:center">Pagamento Confirmado!</h1>
    <p style="color:#64748b">Ola! Recebemos a confirmacao do seu pagamento. Bem-vindo ao <strong>Plano {plano_nome}</strong> da EmotionAI.</p>
    <div style="background:#f8fafc;border-radius:8px;padding:20px;margin:20px 0">
      <p style="margin:5px 0"><strong>Plano:</strong> {plano_nome}</p>
      <p style="margin:5px 0"><strong>Valor:</strong> R$ {valor:.2f}</p>
      <p style="margin:5px 0"><strong>Forma:</strong> PIX</p>
      <p style="margin:5px 0"><strong>ID:</strong> {payment_id}</p>
    </div>
    <p>Seu acesso ao plano <strong>{plano_nome}</strong> ja esta liberado!</p>
    <center>
      <a href="https://emotion-platform-albert.onrender.com/app/dashboard" style="display:inline-block;background:linear-gradient(135deg,#6366f1,#8b5cf6);color:white;padding:14px 32px;border-radius:8px;text-decoration:none;font-weight:600;margin-top:20px">Acessar Dashboard</a>
    </center>
    <p style="color:#94a3b8;font-size:12px;margin-top:30px;text-align:center">EmotionAI - Saude mental com IA</p>
    </div>"""
    return enviar_email(destinatario, f"Pagamento Confirmado - Plano {plano_nome}", html)


from fastapi import APIRouter
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/api/v1/email", tags=["Email"])

@router.get("/teste")
async def teste_endpoint(destinatario: str = ""):
    if not destinatario:
        return {"erro": "passe ?destinatario=seu@email.com"}
    ok = email_pagamento_aprovado(destinatario, "pro", 29.90, "teste123")
    return {"enviado": ok, "destinatario": destinatario, "provider": "brevo"}

class EmailServicePlugin(PluginBase):
    name = "email_service"
    def setup(self, app):
        app.include_router(router)

plugin = EmailServicePlugin()
