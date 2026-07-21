#!/usr/bin/env python3
"""SRQ-20 OMS saúde mental geral"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/srq20", tags=["Avaliacao Avancada"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "srq20_mental_OMS", "status": "ativo",
                          "descricao": "SRQ-20 OMS saúde mental geral",
                          "categoria": "avaliacao_avancada",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "srq20_mental_OMS",
                          "descricao": "SRQ-20 OMS saúde mental geral",
                          "categoria": "avaliacao_avancada",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "srq20_mental_OMS"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
