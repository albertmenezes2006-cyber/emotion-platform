#!/usr/bin/env python3
"""Changelog publico do produto"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/changelog", tags=["Changelog"])

UPDATES = [
    {
        "versao": "v24.4.0",
        "data": "17/07/2026",
        "tipo": "major",
        "items": [
            "PIX integrado para pagamentos instantâneos",
            "Microsoft Clarity para análise de usuários",
            "Widget embeddable para sites de psicólogos",
            "Protocolo de crise com CVV integrado",
            "Sistema de NPS automático",
            "Página de status do sistema",
            "Security headers avançados",
            "Rate limiting melhorado",
            "Compressão GZip ativa",
            "Validação de CRP de psicólogos"
        ]
    },
    {
        "versao": "v24.3.0",
        "data": "16/07/2026",
        "tipo": "major",
        "items": [
            "1461 plugins funcionando",
            "7255 rotas ativas",
            "Testes 100% passando",
            "Deploy estável no Render",
            "Swagger protegido com 4 camadas"
        ]
    }
]

@router.get("", response_class=HTMLResponse)
async def pagina_changelog():
    items_html = ""
    for u in UPDATES:
        cor = "#667eea" if u["tipo"] == "major" else "#38a169"
        li = "".join(f"<li>{i}</li>" for i in u["items"])
        items_html += f"""
        <div style="background:white;border-radius:12px;padding:24px;
                    margin-bottom:16px;box-shadow:0 2px 8px rgba(0,0,0,0.08);
                    border-left:4px solid {cor}">
            <div style="display:flex;justify-content:space-between;align-items:center">
                <h2 style="margin:0;color:{cor}">{u["versao"]}</h2>
                <span style="color:#888;font-size:14px">{u["data"]}</span>
            </div>
            <ul style="margin:12px 0 0;padding-left:20px;color:#555;line-height:1.8">
                {li}
            </ul>
        </div>"""

    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Changelog — Emotion Platform</title>
    <style>body{{font-family:sans-serif;background:#f8f9fa;margin:0;padding:20px}}
    .container{{max-width:700px;margin:0 auto}}
    h1{{color:#333}}</style>
</head>
<body>
<div class="container">
    <h1>📋 Changelog — Emotion Platform</h1>
    <p style="color:#888">Histórico de atualizações e melhorias</p>
    {items_html}
    <div style="text-align:center;padding:20px;color:#aaa;font-size:14px">
        <a href="/">← Voltar ao início</a>
    </div>
</div>
</body>
</html>""")

class ChangelogPlugin(PluginBase):
    name = "changelog_publico"
    def setup(self, app):
        app.include_router(router)

plugin = ChangelogPlugin()
