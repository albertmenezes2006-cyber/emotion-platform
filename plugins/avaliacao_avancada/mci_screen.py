#!/usr/bin/env python3
"""MCI Comprometimento cognitivo leve"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/mci", tags=["Avaliacao Avancada"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "mci_screen", "status": "ativo",
                          "descricao": "MCI Comprometimento cognitivo leve",
                          "categoria": "avaliacao_avancada",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "mci_screen",
                          "descricao": "MCI Comprometimento cognitivo leve",
                          "categoria": "avaliacao_avancada",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "mci_screen"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
