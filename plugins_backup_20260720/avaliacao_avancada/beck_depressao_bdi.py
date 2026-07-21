#!/usr/bin/env python3
"""Beck Depression Inventory BDI-II"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/bdi", tags=["Avaliacao Avancada"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "beck_depressao_bdi", "status": "ativo",
                          "descricao": "Beck Depression Inventory BDI-II",
                          "categoria": "avaliacao_avancada",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "beck_depressao_bdi",
                          "descricao": "Beck Depression Inventory BDI-II",
                          "categoria": "avaliacao_avancada",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "beck_depressao_bdi"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
