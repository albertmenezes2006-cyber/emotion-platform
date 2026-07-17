#!/usr/bin/env python3
"""Serious games saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/serious-games", tags=["Tecnologia Saude"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "serious_games_mental", "status": "ativo",
                          "descricao": "Serious games saúde mental",
                          "categoria": "tecnologia_saude",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "serious_games_mental",
                          "descricao": "Serious games saúde mental",
                          "categoria": "tecnologia_saude",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "serious_games_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
