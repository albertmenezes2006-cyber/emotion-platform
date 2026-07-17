#!/usr/bin/env python3
"""SCS Self-Compassion Scale Neff"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/scs", tags=["Avaliacao Avancada"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "scs_autocompaixao", "status": "ativo",
                          "descricao": "SCS Self-Compassion Scale Neff",
                          "categoria": "avaliacao_avancada",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "scs_autocompaixao",
                          "descricao": "SCS Self-Compassion Scale Neff",
                          "categoria": "avaliacao_avancada",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "scs_autocompaixao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
