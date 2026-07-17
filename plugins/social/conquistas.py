#!/usr/bin/env python3
"""Sistema de conquistas e badges"""
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, HTMLResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import json
from pathlib import Path

router = APIRouter(prefix="/api/v1/conquistas", tags=["Conquistas"])
ARQUIVO = Path("conquistas_usuarios.json")

CONQUISTAS = [
    {"id": "primeiro_phq9", "nome": "Primeiro Passo", "desc": "Completou sua primeira avaliação PHQ-9",
     "icone": "🎯", "xp": 50, "raridade": "comum"},
    {"id": "semana_1", "nome": "Uma Semana", "desc": "7 dias consecutivos usando a plataforma",
     "icone": "🔥", "xp": 100, "raridade": "incomum"},
    {"id": "mes_1", "nome": "Um Mês", "desc": "30 dias de uso contínuo",
     "icone": "⭐", "xp": 300, "raridade": "raro"},
    {"id": "10_avaliacoes", "nome": "Avaliador", "desc": "Realizou 10 avaliações",
     "icone": "📊", "xp": 150, "raridade": "incomum"},
    {"id": "primeiro_chat", "nome": "Conectado", "desc": "Primeira conversa com a IA",
     "icone": "💬", "xp": 30, "raridade": "comum"},
    {"id": "diario_7", "nome": "Escritor", "desc": "7 entradas no diário emocional",
     "icone": "📔", "xp": 70, "raridade": "comum"},
    {"id": "score_baixo", "nome": "Progresso Real", "desc": "PHQ-9 reduziu 5 pontos",
     "icone": "📉", "xp": 200, "raridade": "raro"},
    {"id": "indicou", "nome": "Embaixador", "desc": "Indicou um colega psicólogo",
     "icone": "🤝", "xp": 250, "raridade": "epico"},
    {"id": "plano_pro", "nome": "Profissional", "desc": "Assinou o plano Pro",
     "icone": "💎", "xp": 500, "raridade": "epico"},
    {"id": "100_pacientes", "nome": "Clínica Completa", "desc": "100 pacientes avaliados",
     "icone": "👑", "xp": 1000, "raridade": "lendario"},
]

CORES = {"comum": "#888", "incomum": "#38a169", "raro": "#667eea",
         "epico": "#9333ea", "lendario": "#f59e0b"}

def carregar():
    if ARQUIVO.exists():
        return json.loads(ARQUIVO.read_text())
    return {}

@router.post("/desbloquear/{user_id}/{conquista_id}")
async def desbloquear(user_id: str, conquista_id: str):
    conquista = next((c for c in CONQUISTAS if c["id"] == conquista_id), None)
    if not conquista:
        return JSONResponse({"erro": "Conquista não encontrada"}, status_code=404)
    dados = carregar()
    if user_id not in dados:
        dados[user_id] = []
    if conquista_id not in [c["id"] for c in dados[user_id]]:
        dados[user_id].append({**conquista, "desbloqueado_em": datetime.utcnow().isoformat()})
        ARQUIVO.write_text(json.dumps(dados, ensure_ascii=False, indent=2))
        return JSONResponse({"nova_conquista": True, "conquista": conquista})
    return JSONResponse({"nova_conquista": False, "msg": "Já desbloqueada"})

@router.get("/perfil/{user_id}", response_class=HTMLResponse)
async def perfil_conquistas(user_id: str):
    dados = carregar()
    user_conquistas = {c["id"] for c in dados.get(user_id, [])}
    cards = ""
    for c in CONQUISTAS:
        desbloqueado = c["id"] in user_conquistas
        cor = CORES.get(c["raridade"], "#888")
        opacity = "1" if desbloqueado else "0.3"
        cards += f"""
        <div style="background:white;border-radius:16px;padding:20px;text-align:center;
                    border:2px solid {cor if desbloqueado else '#eee'};
                    opacity:{opacity};transition:all 0.3s">
          <div style="font-size:40px;margin-bottom:8px">{c['icone']}</div>
          <div style="font-weight:700;color:#333;font-size:15px">{c['nome']}</div>
          <div style="color:#888;font-size:13px;margin:4px 0">{c['desc']}</div>
          <div style="background:{cor};color:white;padding:2px 10px;
                      border-radius:20px;font-size:11px;display:inline-block;margin-top:8px">
            {c['raridade'].upper()} · +{c['xp']} XP
          </div>
          {"<div style='color:#38a169;font-size:12px;margin-top:6px'>✅ Desbloqueado</div>" if desbloqueado else ""}
        </div>"""
    total = len(user_conquistas)
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Conquistas — {user_id}</title>
<style>body{{font-family:sans-serif;background:#f8f9fa;padding:20px;margin:0}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:16px;max-width:900px;margin:0 auto}}</style>
</head><body>
<div style="max-width:900px;margin:0 auto">
<a href="/" style="color:#667eea;text-decoration:none">← Voltar</a>
<h1 style="color:#333;margin:16px 0">🏆 Conquistas — {user_id}</h1>
<p style="color:#888;margin-bottom:24px">{total}/{len(CONQUISTAS)} desbloqueadas</p>
<div class="grid">{cards}</div>
</div></body></html>""")

@router.get("/todas")
async def todas_conquistas():
    return JSONResponse(CONQUISTAS)

class ConquistasPlugin(PluginBase):
    name = "sistema_conquistas"
    def setup(self, app): app.include_router(router)
plugin = ConquistasPlugin()
