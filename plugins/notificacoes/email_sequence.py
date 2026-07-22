#!/usr/bin/env python3
"""Sequência automática de 3 emails pós-cadastro"""
from fastapi import APIRouter, BackgroundTasks
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
import httpx, os, asyncio
from datetime import datetime

router = APIRouter(prefix="/api/v1/email-sequence", tags=["Email"])

BREVO_KEY = os.getenv("BREVO_API_KEY", "")
FROM_EMAIL = "albertmenezes2006@gmail.com"
FROM_NAME = "Albert — EmotionAI"
BASE = os.getenv("BASE_URL", "https://emotion-platform-albert.onrender.com")

async def enviar_brevo(para: str, nome: str, assunto: str, html: str):
    if not BREVO_KEY:
        return
    async with httpx.AsyncClient() as client:
        await client.post(
            "https://api.brevo.com/v3/smtp/email",
            headers={"api-key": BREVO_KEY, "Content-Type": "application/json"},
            json={
                "sender": {"name": FROM_NAME, "email": FROM_EMAIL},
                "to": [{"email": para, "name": nome}],
                "subject": assunto,
                "htmlContent": html
            },
            timeout=10
        )

async def sequencia_emails(email: str, nome: str):
    """Envia 3 emails em sequência"""
    primeiro_nome = nome.split()[0] if nome else "Psicólogo"
    
    # Email 1 — imediato (boas-vindas)
    await enviar_brevo(email, nome,
        f"🧠 Bem-vindo ao EmotionAI, {primeiro_nome}!",
        f"""<div style="font-family:Inter,sans-serif;max-width:600px;margin:0 auto;padding:2rem">
        <h1 style="color:#667eea">Olá, {primeiro_nome}! 👋</h1>
        <p>Seja bem-vindo ao EmotionAI — a plataforma que vai transformar sua prática clínica.</p>
        <h3>Por onde começar:</h3>
        <ul>
          <li>✅ <a href="{BASE}/app/avaliacao">Aplique o PHQ-9</a> no seu primeiro paciente</li>
          <li>✅ <a href="{BASE}/app/chat">Converse com a Sofia</a> (nossa IA)</li>
          <li>✅ <a href="{BASE}/app/diario">Configure o diário emocional</a></li>
        </ul>
        <a href="{BASE}/app/dashboard" style="display:inline-block;background:linear-gradient(135deg,#667eea,#764ba2);color:white;padding:12px 24px;border-radius:50px;text-decoration:none;font-weight:700;margin-top:1rem">
          Acessar plataforma →
        </a>
        <p style="color:#718096;font-size:0.85rem;margin-top:2rem">
          Qualquer dúvida, responda este email.<br>— Albert, fundador do EmotionAI
        </p>
        </div>"""
    )
    
    # Email 2 — após 2 dias
    await asyncio.sleep(172800)  # 48 horas
    await enviar_brevo(email, nome,
        f"💡 {primeiro_nome}, você sabia disso no EmotionAI?",
        f"""<div style="font-family:Inter,sans-serif;max-width:600px;margin:0 auto;padding:2rem">
        <h2 style="color:#667eea">Dica especial para você 💡</h2>
        <p>Olá, {primeiro_nome}! Espero que esteja aproveitando o EmotionAI.</p>
        <p><strong>Você sabia?</strong> Com o PHQ-9 digital, seus pacientes respondem <em>antes</em> da sessão e você chega com o score pronto. Isso economiza até 15 minutos por atendimento.</p>
        <p>Calcule: 15 min × 20 pacientes/semana = <strong>5 horas economizadas por semana!</strong></p>
        <a href="{BASE}/app/avaliacao" style="display:inline-block;background:linear-gradient(135deg,#667eea,#764ba2);color:white;padding:12px 24px;border-radius:50px;text-decoration:none;font-weight:700;margin-top:1rem">
          Testar PHQ-9 agora →
        </a>
        </div>"""
    )
    
    # Email 3 — após 5 dias
    await asyncio.sleep(259200)  # 72 horas a mais
    await enviar_brevo(email, nome,
        f"🎁 {primeiro_nome}, presente especial para você",
        f"""<div style="font-family:Inter,sans-serif;max-width:600px;margin:0 auto;padding:2rem">
        <h2 style="color:#667eea">Um presente exclusivo 🎁</h2>
        <p>Olá, {primeiro_nome}! Como você ainda está no plano gratuito, quero te dar uma chance especial.</p>
        <p>Use o cupom <strong style="color:#667eea;font-size:1.2rem">PSICOLOGO</strong> e ganhe <strong>30% de desconto</strong> no plano Pro.</p>
        <p>Com o Pro você tem: prontuário completo, agendamento online e chat IA ilimitado.</p>
        <div style="background:#f8fafc;border:2px dashed #667eea;border-radius:12px;padding:1rem;text-align:center;margin:1rem 0">
          <span style="font-size:1.5rem;font-weight:900;color:#667eea;letter-spacing:0.1em">PSICOLOGO</span>
        </div>
        <a href="{BASE}/planos" style="display:inline-block;background:linear-gradient(135deg,#667eea,#764ba2);color:white;padding:12px 24px;border-radius:50px;text-decoration:none;font-weight:700">
          Resgatar desconto →
        </a>
        <p style="color:#718096;font-size:0.8rem;margin-top:1rem">*Oferta válida por 48 horas.</p>
        </div>"""
    )

@router.post("/iniciar")
async def iniciar_sequencia(
    email: str, nome: str, background_tasks: BackgroundTasks
):
    """Inicia sequência de emails pós-cadastro"""
    background_tasks.add_task(sequencia_emails, email, nome)
    return JSONResponse({"ok": True, "msg": "Sequência iniciada"})

@router.get("/status")
async def status():
    return {"plugin": "email_sequence", "emails": 3, "status": "ativo"}

class EmailSequencePlugin(PluginBase):
    name = "email_sequence_v1"
    def setup(self, app):
        app.include_router(router)

plugin = EmailSequencePlugin()
