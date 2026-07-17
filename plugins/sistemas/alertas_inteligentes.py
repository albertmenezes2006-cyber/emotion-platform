#!/usr/bin/env python3
"""Alertas inteligentes baseados em scores"""
from fastapi import APIRouter, Request, BackgroundTasks
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
import httpx, os
from datetime import datetime

router = APIRouter(prefix="/api/v1/alertas", tags=["Alertas"])

TOKEN = os.getenv("TELEGRAM_TOKEN", "8909749074:AAGNoB-JPZVC0Vl1dYeiN__1ktxza6GZ0s4")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "albertmenezes2006@gmail.com")

async def alerta_telegram(msg: str):
    if not CHAT_ID:
        print(f"[ALERTA] {msg}")
        return
    async with httpx.AsyncClient() as client:
        await client.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "HTML"},
            timeout=5
        )

@router.post("/score-alto")
async def alerta_score_alto(request: Request, bg: BackgroundTasks):
    dados = await request.json()
    score = dados.get("score", 0)
    tipo = dados.get("tipo", "PHQ-9")
    user = dados.get("user_id", "anonimo")
    if score >= 15:
        nivel = "GRAVE" if score >= 20 else "ALTO"
        msg = (f"🚨 <b>ALERTA {nivel} — {tipo}</b>
"
               f"Score: {score}
Usuario: {user}
"
               f"Timestamp: {datetime.utcnow().isoformat()}
"
               f"⚠️ Requer atenção imediata!")
        bg.add_task(alerta_telegram, msg)
        return JSONResponse({"alerta": True, "nivel": nivel,
                             "recursos": {"cvv": "188", "samu": "192",
                                          "chat_cvv": "https://cvv.org.br/chat"}})
    return JSONResponse({"alerta": False, "score": score})

@router.post("/novo-usuario")
async def alerta_novo_usuario(request: Request, bg: BackgroundTasks):
    dados = await request.json()
    msg = (f"🎉 <b>Novo usuario cadastrado!</b>
"
           f"Email: {dados.get('email', 'N/A')}
"
           f"Nome: {dados.get('nome', 'N/A')}
"
           f"Origem: {dados.get('origem', 'site')}
"
           f"Timestamp: {datetime.utcnow().isoformat()}")
    bg.add_task(alerta_telegram, msg)
    return JSONResponse({"ok": True})

@router.post("/novo-pagamento")
async def alerta_novo_pagamento(request: Request, bg: BackgroundTasks):
    dados = await request.json()
    msg = (f"💰 <b>NOVO PAGAMENTO!</b>
"
           f"Plano: {dados.get('plano', 'N/A')}
"
           f"Valor: R$ {dados.get('valor', 0)}
"
           f"Email: {dados.get('email', 'N/A')}
"
           f"🎊 Receita gerada!")
    bg.add_task(alerta_telegram, msg)
    return JSONResponse({"ok": True})

@router.get("/testar")
async def testar_alertas(bg: BackgroundTasks):
    bg.add_task(alerta_telegram,
        "🧪 <b>Teste de alertas</b>
✅ Sistema funcionando!
"
        f"Timestamp: {datetime.utcnow().isoformat()}")
    return JSONResponse({"ok": True, "msg": "Alerta de teste enviado"})

class AlertasPlugin(PluginBase):
    name = "alertas_inteligentes"
    def setup(self, app):
        app.include_router(router)

plugin = AlertasPlugin()
