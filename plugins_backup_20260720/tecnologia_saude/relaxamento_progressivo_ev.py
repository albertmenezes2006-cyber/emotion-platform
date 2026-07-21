#!/usr/bin/env python3
"""PMR evidências científicas"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/pmr-ev", tags=["Tecnologia Saude"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "relaxamento_progressivo_ev", "status": "ativo",
                          "descricao": "PMR evidências científicas",
                          "categoria": "tecnologia_saude",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "relaxamento_progressivo_ev",
                          "descricao": "PMR evidências científicas",
                          "categoria": "tecnologia_saude",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "relaxamento_progressivo_ev"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
