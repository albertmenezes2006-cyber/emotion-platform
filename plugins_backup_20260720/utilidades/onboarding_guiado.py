#!/usr/bin/env python3
"""Onboarding guiado para novos usuarios"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/onboarding", tags=["Onboarding"])

PASSOS = [
    {"id": 1, "titulo": "Bem-vindo!", "descricao": "Conheça a plataforma", "url": "/", "icone": "🧠"},
    {"id": 2, "titulo": "Sua primeira avaliação", "descricao": "Aplique o PHQ-9", "url": "/app/avaliacao", "icone": "📊"},
    {"id": 3, "titulo": "Chat com IA", "descricao": "Converse com nossa IA", "url": "/app/chat", "icone": "💬"},
    {"id": 4, "titulo": "Diário emocional", "descricao": "Registre seu estado", "url": "/app/diario", "icone": "📔"},
    {"id": 5, "titulo": "Dashboard", "descricao": "Veja sua evolução", "url": "/app/dashboard", "icone": "📈"},
    {"id": 6, "titulo": "Planos", "descricao": "Escolha seu plano", "url": "/app/planos", "icone": "⭐"},
]

@router.get("", response_class=HTMLResponse)
async def pagina_onboarding():
    passos_html = ""
    for p in PASSOS:
        passos_html += f"""
        <div class="passo" onclick="irPara('{p['url']}', {p['id']})">
            <div class="icone">{p['icone']}</div>
            <div class="info">
                <h3>{p['titulo']}</h3>
                <p>{p['descricao']}</p>
            </div>
            <div class="arrow">→</div>
        </div>"""

    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Primeiros Passos — Emotion Platform</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: sans-serif; background: linear-gradient(135deg, #667eea, #764ba2);
               min-height: 100vh; padding: 20px; }}
        .container {{ max-width: 600px; margin: 0 auto; }}
        h1 {{ color: white; text-align: center; font-size: 28px; margin-bottom: 8px; }}
        .sub {{ color: rgba(255,255,255,0.8); text-align: center; margin-bottom: 24px; }}
        .progresso {{ background: rgba(255,255,255,0.2); border-radius: 20px;
                     height: 8px; margin-bottom: 24px; overflow: hidden; }}
        .progresso-bar {{ background: white; height: 100%; border-radius: 20px;
                         transition: width 0.5s; width: 0%; }}
        .passo {{ background: white; border-radius: 16px; padding: 20px;
                 margin-bottom: 12px; display: flex; align-items: center;
                 gap: 16px; cursor: pointer; transition: transform 0.2s;
                 border: 3px solid transparent; }}
        .passo:hover {{ transform: translateX(4px); border-color: #667eea; }}
        .passo.concluido {{ opacity: 0.7; background: #f0fff4; border-color: #38a169; }}
        .icone {{ font-size: 32px; width: 50px; text-align: center; }}
        .info h3 {{ color: #333; font-size: 16px; }}
        .info p {{ color: #888; font-size: 14px; margin-top: 4px; }}
        .arrow {{ margin-left: auto; font-size: 20px; color: #667eea; font-weight: 700; }}
        .concluido .arrow {{ color: #38a169; }}
    </style>
</head>
<body>
<div class="container">
    <h1>🚀 Primeiros Passos</h1>
    <p class="sub">Complete cada etapa para dominar a plataforma</p>
    <div class="progresso"><div class="progresso-bar" id="barra"></div></div>
    {passos_html}
</div>
<script>
var concluidos = JSON.parse(localStorage.getItem('onboarding') || '[]');
function atualizar() {{
    var pct = (concluidos.length / {len(PASSOS)}) * 100;
    document.getElementById('barra').style.width = pct + '%';
    document.querySelectorAll('.passo').forEach(function(p, i) {{
        if (concluidos.includes(i+1)) p.classList.add('concluido');
    }});
}}
function irPara(url, id) {{
    if (!concluidos.includes(id)) concluidos.push(id);
    localStorage.setItem('onboarding', JSON.stringify(concluidos));
    atualizar();
    setTimeout(function() {{ window.location.href = url; }}, 300);
}}
atualizar();
</script>
</body>
</html>""")

@router.get("/status")
async def status_onboarding():
    return JSONResponse({"passos": PASSOS, "total": len(PASSOS)})

class OnboardingPlugin(PluginBase):
    name = "onboarding_guiado"
    def setup(self, app):
        app.include_router(router)

plugin = OnboardingPlugin()
