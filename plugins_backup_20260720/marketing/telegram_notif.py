#!/usr/bin/env python3
"""Notificacoes Telegram para o admin"""
from fastapi import APIRouter, BackgroundTasks
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
import httpx
import os

router = APIRouter(prefix="/api/v1/telegram", tags=["Telegram"])

TOKEN = os.getenv("TELEGRAM_TOKEN", "8909749074:AAGNoB-JPZVC0Vl1dYeiN__1ktxza6GZ0s4")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

async def enviar_telegram(mensagem: str):
    if not CHAT_ID:
        print(f"[TELEGRAM] {mensagem}")
        return False
    async with httpx.AsyncClient() as client:
        r = await client.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            json={"chat_id": CHAT_ID, "text": mensagem, "parse_mode": "HTML"},
            timeout=10
        )
        return r.status_code == 200

@router.post("/notificar")
async def notificar(mensagem: str, bg: BackgroundTasks):
    bg.add_task(enviar_telegram, mensagem)
    return JSONResponse({"ok": True})

@router.get("/setup")
async def setup_telegram():
    return {
        "instrucoes": [
            "1. Abra @userinfobot no Telegram",
            "2. Envie qualquer mensagem",
            "3. Copie seu chat_id",
            "4. Adicione TELEGRAM_CHAT_ID no Render"
        ],
        "token_configurado": bool(TOKEN),
        "chat_id_configurado": bool(CHAT_ID)
    }

@router.get("/teste")
async def teste_telegram(bg: BackgroundTasks):
    bg.add_task(enviar_telegram,
        "🧠 <b>Emotion Platform</b>\n✅ Telegram funcionando!\n🚀 Notificacoes ativas")
    return JSONResponse({"ok": True, "msg": "Mensagem enviada"})

class TelegramPlugin(PluginBase):
    name = "telegram_notif"
    def setup(self, app):
        app.include_router(router)

plugin = TelegramPlugin()
