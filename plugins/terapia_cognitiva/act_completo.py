#!/usr/bin/env python3
"""ACT — Acceptance and Commitment Therapy ferramentas"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/act", tags=["ACT"])

PROCESSOS = [
    {"nome": "Aceitação", "icone": "🌊", "cor": "#667eea",
     "desc": "Abrir espaço para pensamentos e sentimentos difíceis sem lutar contra eles",
     "exercicio": "Imagine seus pensamentos como ondas do mar. Observe-os chegando e indo. Você não precisa nadar contra eles.",
     "pratica": "Diga: 'Estou tendo o pensamento de que...' em vez de 'Penso que...'"},
    {"nome": "Defusão Cognitiva", "icone": "☁️", "cor": "#764ba2",
     "desc": "Criar distância de pensamentos, vendo-os como eventos mentais, não verdades",
     "exercicio": "Pegue um pensamento difícil. Repita-o rapidamente por 30 segundos. Observe como perde poder.",
     "pratica": "Visualize pensamentos como legendas de um filme que você está assistindo"},
    {"nome": "Momento Presente", "icone": "🎯", "cor": "#38a169",
     "desc": "Estar em contato com o aqui e agora, com abertura e curiosidade",
     "exercicio": "5-4-3-2-1: Nomeie 5 coisas que vê, 4 que toca, 3 que ouve, 2 que cheira, 1 que saboreia.",
     "pratica": "Pratique 5 minutos de atenção plena a uma atividade rotineira"},
    {"nome": "Eu Como Contexto", "icone": "👁️", "cor": "#e53e3e",
     "desc": "Perceber que você é mais do que seus pensamentos e sentimentos",
     "exercicio": "Feche os olhos. Observe que há uma parte de você que observa tudo. Essa é a sua consciência.",
     "pratica": "Pergunte: 'Quem está observando meus pensamentos?'"},
    {"nome": "Valores", "icone": "⭐", "cor": "#f59e0b",
     "desc": "Clarificar o que realmente importa para você como direção de vida",
     "exercicio": "Imagine seu funeral. O que você gostaria que as pessoas dissessem sobre quem você foi?",
     "pratica": "Liste seus 3 valores mais importantes e 1 ação alinhada a cada um"},
    {"nome": "Ação Comprometida", "icone": "🚀", "cor": "#3182ce",
     "desc": "Agir de acordo com seus valores mesmo na presença de dificuldades",
     "exercicio": "Escolha um valor. Defina uma ação pequena e concreta que você fará HOJE alinhada a esse valor.",
     "pratica": "Use: 'Quando X acontecer, eu farei Y para honrar meu valor de Z'"},
]

@router.get("", response_class=HTMLResponse)
async def pagina_act():
    cards = ""
    for p in PROCESSOS:
        cards += f"""
        <div style="background:white;border-radius:20px;padding:28px;margin-bottom:20px;
                    box-shadow:0 4px 20px rgba(0,0,0,0.08);border-left:5px solid {p['cor']}">
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px">
            <span style="font-size:32px">{p['icone']}</span>
            <h2 style="color:{p['cor']};margin:0">{p['nome']}</h2>
          </div>
          <p style="color:#555;line-height:1.7;margin-bottom:16px">{p['desc']}</p>
          <details style="margin-bottom:12px">
            <summary style="cursor:pointer;color:{p['cor']};font-weight:700;padding:8px 0">
              🎯 Exercício prático
            </summary>
            <div style="background:#f8f9fa;border-radius:8px;padding:14px;margin-top:8px">
              <p style="color:#555;margin:0;line-height:1.7">{p['exercicio']}</p>
            </div>
          </details>
          <div style="background:{p['cor']}15;border-radius:8px;padding:12px;
                      border-left:3px solid {p['cor']}">
            <strong style="color:{p['cor']}">💡 Prática diária:</strong>
            <p style="color:#555;margin:4px 0 0;font-size:14px">{p['pratica']}</p>
          </div>
        </div>"""
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>ACT — Acceptance and Commitment Therapy</title>
<style>body{{font-family:sans-serif;background:#f8f9fa;padding:20px;margin:0}}
.container{{max-width:700px;margin:0 auto}}
details summary::-webkit-details-marker{{display:none}}
</style></head><body><div class="container">
<a href="/" style="color:#667eea;text-decoration:none">← Voltar</a>
<h1 style="color:#333;margin:16px 0">🌱 ACT — Terapia de Aceitação e Compromisso</h1>
<p style="color:#888;margin-bottom:28px">Os 6 processos centrais para uma vida psicológica plena</p>
{cards}
<div style="background:linear-gradient(135deg,#667eea,#764ba2);border-radius:16px;
            padding:24px;text-align:center;color:white;margin-top:8px">
  <h2 style="margin:0 0 8px">Pratique ACT com suporte profissional</h2>
  <p style="opacity:0.9;margin:0 0 16px">Um psicólogo treinado em ACT pode guiar seu processo</p>
  <a href="/api/v1/agenda/pagina" style="background:white;color:#667eea;padding:12px 24px;
     border-radius:8px;text-decoration:none;font-weight:700">📅 Agendar sessão</a>
</div>
</div></body></html>""")

@router.get("/processos")
async def listar_processos():
    return JSONResponse([{"nome": p["nome"], "desc": p["desc"],
                          "pratica": p["pratica"]} for p in PROCESSOS])

class ACTPlugin(PluginBase):
    name = "act_completo"
    def setup(self, app): app.include_router(router)
plugin = ACTPlugin()
