"""Serviço de email via Gmail SMTP"""
import os
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

logger = logging.getLogger(__name__)

GMAIL_USER = os.getenv("GMAIL_USER", "albertmenezes2006@gmail.com")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD", "")

def enviar_email(destinatario: str, assunto: str, html: str) -> bool:
    if not GMAIL_APP_PASSWORD:
        logger.warning("GMAIL_APP_PASSWORD nao configurado")
        return False
    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = assunto
        msg["From"] = f"EmotionAI <{GMAIL_USER}>"
        msg["To"] = destinatario
        msg.attach(MIMEText(html, "html", "utf-8"))
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=15) as server:
            server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
            server.send_message(msg)
        return True
    except Exception as e:
        logger.error(f"Erro email: {e}")
        return False

def email_pagamento_aprovado(destinatario, plano, valor, payment_id):
    plano_nome = "Pro" if plano == "pro" else "Clinica" if plano == "clinica" else plano.title()
    html = f"""<div style="font-family:sans-serif;max-width:560px;margin:auto;padding:30px;background:#fff;border-radius:12px">
    <h1 style="color:#6366f1">Pagamento Confirmado!</h1>
    <p>Ola! Recebemos a confirmacao do seu pagamento.</p>
    <p><strong>Plano:</strong> {plano_nome}<br><strong>Valor:</strong> R$ {valor:.2f}<br><strong>ID:</strong> {payment_id}</p>
    <p>Seu acesso ao plano <strong>{plano_nome}</strong> ja esta liberado!</p>
    <a href="https://emotion-platform-albert.onrender.com/app/dashboard" style="display:inline-block;background:#6366f1;color:white;padding:12px 24px;border-radius:8px;text-decoration:none;margin-top:20px">Acessar Dashboard</a>
    <p style="color:#94a3b8;font-size:12px;margin-top:30px">EmotionAI - Saude mental com IA</p>
    </div>"""
    return enviar_email(destinatario, f"Pagamento Confirmado - Plano {plano_nome}", html)
