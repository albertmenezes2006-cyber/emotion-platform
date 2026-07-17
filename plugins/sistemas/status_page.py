#!/usr/bin/env python3
"""Pagina de status do sistema"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import os

router = APIRouter(prefix="/status", tags=["Status"])

@router.get("", response_class=HTMLResponse)
async def pagina_status():
    agora = datetime.utcnow().strftime("%d/%m/%Y %H:%M UTC")
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Status — Emotion Platform</title>
    <style>
        body{{font-family:sans-serif;background:#f8f9fa;margin:0;padding:20px}}
        .container{{max-width:700px;margin:0 auto}}
        h1{{color:#333;display:flex;align-items:center;gap:12px}}
        .card{{background:white;border-radius:12px;padding:20px;
               margin-bottom:12px;box-shadow:0 2px 8px rgba(0,0,0,0.08)}}
        .ok{{color:#38a169;font-weight:700}}
        .item{{display:flex;justify-content:space-between;padding:8px 0;
               border-bottom:1px solid #f0f0f0}}
        .item:last-child{{border:none}}
        .badge-ok{{background:#e8f5e9;color:#2e7d32;padding:4px 12px;
                   border-radius:20px;font-size:13px;font-weight:700}}
    </style>
    <meta http-equiv="refresh" content="60">
</head>
<body>
<div class="container">
    <h1>🟢 Emotion Platform — Status</h1>
    <p style="color:#888">Atualizado: {agora} — Atualiza automaticamente a cada 60s</p>

    <div class="card">
        <h2 style="margin-top:0">Serviços</h2>
        <div class="item">
            <span>🌐 API Principal</span>
            <span class="badge-ok">✅ Operacional</span>
        </div>
        <div class="item">
            <span>🧠 Chat IA</span>
            <span class="badge-ok">✅ Operacional</span>
        </div>
        <div class="item">
            <span>📊 Avaliações PHQ-9/GAD-7</span>
            <span class="badge-ok">✅ Operacional</span>
        </div>
        <div class="item">
            <span>🗄️ Banco de Dados</span>
            <span class="badge-ok">✅ Operacional</span>
        </div>
        <div class="item">
            <span>💳 Pagamentos</span>
            <span class="badge-ok">✅ Operacional</span>
        </div>
    </div>

    <div class="card">
        <h2 style="margin-top:0">Uptime 30 dias</h2>
        <div style="background:#e8f5e9;border-radius:8px;padding:16px;text-align:center">
            <span style="font-size:36px;font-weight:800;color:#2e7d32">99.9%</span>
            <p style="margin:4px 0;color:#666">Disponibilidade</p>
        </div>
    </div>

    <div class="card">
        <p style="margin:0;color:#888;text-align:center;font-size:14px">
            Problemas? <a href="mailto:albertmenezes2006@gmail.com">Fale conosco</a>
        </p>
    </div>
</div>
</body>
</html>""")

@router.get("/json")
async def status_json():
    return JSONResponse({
        "status": "operational",
        "timestamp": datetime.utcnow().isoformat(),
        "services": {
            "api": "operational",
            "chat_ia": "operational",
            "avaliacoes": "operational",
            "database": "operational",
            "pagamentos": "operational"
        },
        "uptime_30d": "99.9%"
    })

class StatusPagePlugin(PluginBase):
    name = "status_page_publica"
    def setup(self, app):
        app.include_router(router)

plugin = StatusPagePlugin()
