#!/usr/bin/env python3
"""CAGE triagem alcoolismo"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/cage", tags=["Avaliacao Avancada"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "cage_alcool", "status": "ativo",
                          "descricao": "CAGE triagem alcoolismo",
                          "categoria": "avaliacao_avancada",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "cage_alcool",
                          "descricao": "CAGE triagem alcoolismo",
                          "categoria": "avaliacao_avancada",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "cage_alcool"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
