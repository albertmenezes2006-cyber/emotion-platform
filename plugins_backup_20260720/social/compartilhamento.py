#!/usr/bin/env python3
"""Compartilhamento social de resultados"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/api/v1/compartilhar", tags=["Social"])

@router.get("/resultado")
async def compartilhar_resultado(score: int = 0, tipo: str = "phq9"):
    url = f"https://emotion-platform-albert.onrender.com/app/avaliacao"
    texto = f"Acabei de fazer minha avaliação de saúde mental no Emotion Platform. Cuide da sua saúde mental! 🧠"
    return JSONResponse({
        "whatsapp": f"https://wa.me/?text={texto} {url}",
        "linkedin": f"https://www.linkedin.com/sharing/share-offsite/?url={url}",
        "twitter": f"https://twitter.com/intent/tweet?text={texto}&url={url}",
        "telegram": f"https://t.me/share/url?url={url}&text={texto}",
        "email": f"mailto:?subject=Avaliação de Saúde Mental&body={texto} {url}"
    })

@router.get("/badge/{tipo}/{score}", response_class=HTMLResponse)
async def badge_resultado(tipo: str, score: int):
    niveis = {
        "phq9": {0: ("Sem depressão", "#38a169"), 5: ("Depressão leve", "#d69e2e"),
                 10: ("Depressão moderada", "#dd6b20"), 15: ("Depressão grave", "#e53e3e")},
        "gad7": {0: ("Sem ansiedade", "#38a169"), 5: ("Ansiedade leve", "#d69e2e"),
                 10: ("Ansiedade moderada", "#dd6b20"), 15: ("Ansiedade grave", "#e53e3e")}
    }
    escala = niveis.get(tipo, niveis["phq9"])
    nivel_txt, cor = "Avaliado", "#667eea"
    for limiar, (txt, c) in sorted(escala.items()):
        if score >= limiar:
            nivel_txt, cor = txt, c
    return HTMLResponse(f"""
<div style="background:{cor};color:white;padding:16px 24px;border-radius:12px;
            font-family:sans-serif;display:inline-block;text-align:center">
    <div style="font-size:12px;opacity:0.8">{tipo.upper()} Score</div>
    <div style="font-size:32px;font-weight:800">{score}</div>
    <div style="font-size:14px;margin-top:4px">{nivel_txt}</div>
    <div style="font-size:11px;opacity:0.7;margin-top:8px">emotion-platform-albert.onrender.com</div>
</div>""")

class SocialPlugin(PluginBase):
    name = "compartilhamento_social"
    def setup(self, app):
        app.include_router(router)

plugin = SocialPlugin()
