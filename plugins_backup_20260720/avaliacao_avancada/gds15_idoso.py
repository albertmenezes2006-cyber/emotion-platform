#!/usr/bin/env python3
"""GDS-15 depressão geriátrica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/gds15", tags=["Avaliacao Avancada"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "gds15_idoso", "status": "ativo",
                          "descricao": "GDS-15 depressão geriátrica",
                          "categoria": "avaliacao_avancada",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "gds15_idoso",
                          "descricao": "GDS-15 depressão geriátrica",
                          "categoria": "avaliacao_avancada",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "gds15_idoso"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
