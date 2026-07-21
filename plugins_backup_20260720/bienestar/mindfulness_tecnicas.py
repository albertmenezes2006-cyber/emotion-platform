#!/usr/bin/env python3
"""Tecnicas de mindfulness baseadas em evidencias"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/mindfulness", tags=["Mindfulness"])

TECNICAS = [
    {"nome": "Body Scan", "duracao": "15-45 min", "nivel": "Iniciante", "icone": "🧘",
     "desc": "Percorrer o corpo sistematicamente com atenção, observando sensações sem julgamento.",
     "passos": ["Deite-se confortavelmente", "Feche os olhos e respire profundamente 3 vezes",
                "Comece pelos dedos dos pés — observe calor, tensão, formigamento",
                "Suba lentamente pelos pés, tornozelos, pernas...",
                "Continue até o topo da cabeça", "Se distrair, retorne gentilmente sem julgamento"]},
    {"nome": "Raisin Exercise", "duracao": "5-10 min", "nivel": "Iniciante", "icone": "🍇",
     "desc": "Exercício clássico do MBSR: comer uma passa com atenção plena a todos os sentidos.",
     "passos": ["Pegue uma passa (ou qualquer alimento pequeno)", "Observe como ela parece — cor, forma, textura",
                "Cheire devagar e perceba os aromas", "Coloque na língua sem morder ainda",
                "Note a salivação e as primeiras sensações", "Mastigue lentamente, percebendo cada detalhe"]},
    {"nome": "3 Minutos de Respiração", "duracao": "3 min", "nivel": "Iniciante", "icone": "⏱️",
     "desc": "Mini-prática de 3 etapas de 1 minuto cada. Ideal para momentos de estresse.",
     "passos": ["Minuto 1 — Conscientização: 'O que estou pensando, sentindo, notando?'",
                "Minuto 2 — Foco: Concentre toda atenção na respiração",
                "Minuto 3 — Expansão: Expanda a consciência para o corpo todo e ao redor"]},
    {"nome": "Caminhada Consciente", "duracao": "10-30 min", "nivel": "Intermediário", "icone": "🚶",
     "desc": "Praticar mindfulness durante a caminhada, focando nas sensações do movimento.",
     "passos": ["Comece devagar, mais lento que o normal", "Sinta cada passo — calcanhar, planta, dedos",
                "Note o balançar dos braços, o equilíbrio do corpo",
                "Observe o ambiente com curiosidade (sons, cheiros, visão)",
                "Quando a mente divagar, retorne às sensações dos pés no chão"]},
]

@router.get("", response_class=HTMLResponse)
async def pagina_mindfulness():
    cards = ""
    for t in TECNICAS:
        passos_html = "".join(f'<li style="padding:6px 0;color:#555;line-height:1.6">{p}</li>' for p in t["passos"])
        cards += f"""
        <div style="background:white;border-radius:20px;padding:28px;margin-bottom:20px;
                    box-shadow:0 4px 20px rgba(0,0,0,0.08)">
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px">
            <span style="font-size:36px">{t['icone']}</span>
            <div>
              <h2 style="color:#333;margin:0">{t['nome']}</h2>
              <div style="display:flex;gap:8px;margin-top:4px">
                <span style="background:#e8f0fe;color:#667eea;padding:2px 10px;border-radius:20px;font-size:12px">⏱️ {t['duracao']}</span>
                <span style="background:#e8f5e9;color:#38a169;padding:2px 10px;border-radius:20px;font-size:12px">{t['nivel']}</span>
              </div>
            </div>
          </div>
          <p style="color:#666;line-height:1.7;margin-bottom:16px">{t['desc']}</p>
          <details>
            <summary style="cursor:pointer;color:#667eea;font-weight:700;padding:8px 0;list-style:none">
              ▶ Ver passo a passo
            </summary>
            <ol style="margin:12px 0 0;padding-left:20px">{passos_html}</ol>
          </details>
        </div>"""
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Mindfulness — Emotion Platform</title>
<style>body{{font-family:sans-serif;background:#f0f4ff;padding:20px;margin:0}}
.container{{max-width:700px;margin:0 auto}}
details summary::-webkit-details-marker{{display:none}}</style>
</head><body><div class="container">
<a href="/" style="color:#667eea;text-decoration:none">← Voltar</a>
<h1 style="color:#333;margin:16px 0">🧘 Técnicas de Mindfulness</h1>
<p style="color:#888;margin-bottom:24px">Práticas baseadas em MBSR — Mindfulness-Based Stress Reduction</p>
{cards}
<div style="text-align:center;padding:20px;background:white;border-radius:16px;
            box-shadow:0 4px 20px rgba(0,0,0,0.08)">
  <p style="color:#666;margin:0 0 12px">Combine mindfulness com</p>
  <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap">
    <a href="/respiracao" style="background:#667eea;color:white;padding:10px 20px;border-radius:8px;text-decoration:none;font-weight:700">🫁 Respiração</a>
    <a href="/meditacao" style="background:#764ba2;color:white;padding:10px 20px;border-radius:8px;text-decoration:none;font-weight:700">⏱️ Meditação</a>
    <a href="/gratidao" style="background:#f59e0b;color:white;padding:10px 20px;border-radius:8px;text-decoration:none;font-weight:700">💛 Gratidão</a>
  </div>
</div>
</div></body></html>""")

class MindfulnessPlugin(PluginBase):
    name = "mindfulness_tecnicas"
    def setup(self, app): app.include_router(router)
plugin = MindfulnessPlugin()
