#!/usr/bin/env python3
"""Protocolo de crise — CVV integrado"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/api/v1/crise", tags=["Crise"])

@router.get("/ajuda", response_class=HTMLResponse)
async def pagina_crise():
    return HTMLResponse("""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Precisa de Ajuda? — Emotion Platform</title>
    <style>
        body { font-family: sans-serif; background: #fff5f5; margin: 0; padding: 20px; }
        .container { max-width: 600px; margin: 0 auto; }
        .card { background: white; border-radius: 16px; padding: 32px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.1); margin-bottom: 16px; }
        .urgente { background: #fff0f0; border-left: 4px solid #e53e3e; }
        h1 { color: #e53e3e; margin: 0 0 8px; }
        .btn { display: block; background: #e53e3e; color: white;
               text-decoration: none; padding: 16px; border-radius: 12px;
               text-align: center; font-size: 20px; font-weight: 700;
               margin: 16px 0; }
        .btn-green { background: #38a169; }
        .btn-blue { background: #3182ce; }
        p { color: #666; line-height: 1.6; }
    </style>
</head>
<body>
    <div class="container">
        <div class="card urgente">
            <h1>🆘 Você não está sozinho</h1>
            <p>Se você está em crise ou pensando em se machucar,
               ajuda profissional está disponível AGORA:</p>
            <a href="tel:188" class="btn">📞 CVV — Ligue 188 (24h gratuito)</a>
            <a href="https://cvv.org.br/chat" class="btn btn-green" target="_blank">
                💬 Chat CVV — cvv.org.br
            </a>
        </div>
        <div class="card">
            <h2>🏥 Outros recursos</h2>
            <a href="tel:192" class="btn btn-blue">🚑 SAMU — 192</a>
            <a href="tel:190" class="btn" style="background:#805ad5">🚔 Bombeiros — 193</a>
            <p style="margin-top:16px">
                <strong>CAPS:</strong> Centro de Atenção Psicossocial da sua cidade<br>
                <strong>UBS:</strong> Unidade Básica de Saúde mais próxima<br>
                <strong>NASF:</strong> Núcleo de Apoio à Saúde da Família
            </p>
        </div>
    </div>
</body>
</html>""")

@router.get("/banner")
async def banner_crise():
    return {
        "cvv": "188",
        "chat": "https://cvv.org.br/chat",
        "samu": "192",
        "mensagem": "Voce nao esta sozinho. Ajuda disponivel 24h."
    }

class CrisePlugin(PluginBase):
    name = "crise_cvv"
    def setup(self, app):
        app.include_router(router)

plugin = CrisePlugin()
