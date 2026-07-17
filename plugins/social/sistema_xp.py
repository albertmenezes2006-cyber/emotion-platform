#!/usr/bin/env python3
"""Sistema de XP e niveis"""
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, HTMLResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import json
from pathlib import Path

router = APIRouter(prefix="/api/v1/xp", tags=["XP"])
ARQUIVO = Path("xp_usuarios.json")

NIVEIS = [
    {"nivel": 1, "nome": "Iniciante", "xp_min": 0, "icone": "🌱"},
    {"nivel": 2, "nome": "Explorador", "xp_min": 100, "icone": "🔍"},
    {"nivel": 3, "nome": "Comprometido", "xp_min": 300, "icone": "💪"},
    {"nivel": 4, "nome": "Dedicado", "xp_min": 600, "icone": "⭐"},
    {"nivel": 5, "nome": "Expert", "xp_min": 1000, "icone": "🏆"},
    {"nivel": 6, "nome": "Mestre", "xp_min": 2000, "icone": "👑"},
]

ACOES_XP = {
    "avaliacao_phq9": 50, "avaliacao_gad7": 50,
    "entrada_diario": 20, "chat_ia": 10,
    "login_diario": 5, "completar_perfil": 100,
    "indicar_amigo": 200, "assinar_plano": 500
}

def carregar():
    if ARQUIVO.exists():
        return json.loads(ARQUIVO.read_text())
    return {}

def calcular_nivel(xp: int) -> dict:
    nivel_atual = NIVEIS[0]
    proximo = NIVEIS[1] if len(NIVEIS) > 1 else None
    for i, n in enumerate(NIVEIS):
        if xp >= n["xp_min"]:
            nivel_atual = n
            proximo = NIVEIS[i+1] if i+1 < len(NIVEIS) else None
    progresso = 0
    if proximo:
        xp_nivel = xp - nivel_atual["xp_min"]
        xp_necessario = proximo["xp_min"] - nivel_atual["xp_min"]
        progresso = min(100, int((xp_nivel / xp_necessario) * 100))
    return {"nivel": nivel_atual, "proximo": proximo, "progresso": progresso}

@router.post("/ganhar/{user_id}/{acao}")
async def ganhar_xp(user_id: str, acao: str):
    pontos = ACOES_XP.get(acao, 10)
    dados = carregar()
    if user_id not in dados:
        dados[user_id] = {"xp": 0, "acoes": [], "criado": datetime.utcnow().isoformat()}
    dados[user_id]["xp"] += pontos
    dados[user_id]["acoes"].append({"acao": acao, "xp": pontos, "ts": datetime.utcnow().isoformat()})
    ARQUIVO.write_text(json.dumps(dados, ensure_ascii=False, indent=2))
    info = calcular_nivel(dados[user_id]["xp"])
    return JSONResponse({"xp_ganho": pontos, "xp_total": dados[user_id]["xp"],
                         "nivel": info["nivel"], "progresso": info["progresso"]})

@router.get("/perfil/{user_id}")
async def perfil_xp(user_id: str):
    dados = carregar()
    u = dados.get(user_id, {"xp": 0, "acoes": []})
    info = calcular_nivel(u["xp"])
    return JSONResponse({"xp_total": u["xp"], "nivel": info["nivel"],
                         "proximo_nivel": info["proximo"],
                         "progresso": info["progresso"],
                         "acoes_possiveis": ACOES_XP})

@router.get("/ranking")
async def ranking_xp():
    dados = carregar()
    rank = sorted(dados.items(), key=lambda x: x[1]["xp"], reverse=True)[:10]
    return JSONResponse([{"user": u, "xp": d["xp"],
                          "nivel": calcular_nivel(d["xp"])["nivel"]} for u, d in rank])

class XPPlugin(PluginBase):
    name = "sistema_xp"
    def setup(self, app):
        app.include_router(router)

plugin = XPPlugin()
