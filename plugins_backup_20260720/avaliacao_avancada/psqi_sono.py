#!/usr/bin/env python3
"""Pittsburgh Sleep Quality Index"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/psqi", tags=["Avaliacao Avancada"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "psqi_sono", "status": "ativo",
                          "descricao": "Pittsburgh Sleep Quality Index",
                          "categoria": "avaliacao_avancada",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "psqi_sono",
                          "descricao": "Pittsburgh Sleep Quality Index",
                          "categoria": "avaliacao_avancada",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "psqi_sono"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
