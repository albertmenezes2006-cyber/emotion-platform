#!/usr/bin/env python3
"""MoCA avaliação cognitiva"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/moca", tags=["Avaliacao Avancada"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "moca_cognitiva", "status": "ativo",
                          "descricao": "MoCA avaliação cognitiva",
                          "categoria": "avaliacao_avancada",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "moca_cognitiva",
                          "descricao": "MoCA avaliação cognitiva",
                          "categoria": "avaliacao_avancada",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "moca_cognitiva"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
