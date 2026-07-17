#!/usr/bin/env python3
"""Beck Anxiety Inventory"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/bai-beck", tags=["Avaliacao Avancada"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "bai_beck_ansiedade", "status": "ativo",
                          "descricao": "Beck Anxiety Inventory",
                          "categoria": "avaliacao_avancada",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "bai_beck_ansiedade",
                          "descricao": "Beck Anxiety Inventory",
                          "categoria": "avaliacao_avancada",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "bai_beck_ansiedade"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
