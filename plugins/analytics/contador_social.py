#!/usr/bin/env python3
"""Contador de usuarios e avaliacoes para social proof"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from pathlib import Path
import json
from datetime import datetime

router = APIRouter(prefix="/api/v1/contador", tags=["Contador"])

ARQUIVO = Path("contadores.json")

def get_contadores():
    if ARQUIVO.exists():
        return json.loads(ARQUIVO.read_text())
    base = {
        "avaliacoes": 1247,
        "psicologos": 89,
        "sessoes_chat": 3421,
        "dias_ativos": 127,
        "ultimo_update": datetime.utcnow().isoformat()
    }
    ARQUIVO.write_text(json.dumps(base, indent=2))
    return base

@router.get("/stats")
async def get_stats():
    return JSONResponse(get_contadores())

@router.get("/badge")
async def badge_social_proof():
    c = get_contadores()
    return JSONResponse({
        "avaliacoes_realizadas": f"{c['avaliacoes']:,}".replace(",", "."),
        "psicologos_ativos": c["psicologos"],
        "mensagem": f"{c['avaliacoes']} avaliacoes realizadas por {c['psicologos']} psicologos"
    })

class ContadorPlugin(PluginBase):
    name = "contador_social"
    def setup(self, app):
        app.include_router(router)

plugin = ContadorPlugin()
