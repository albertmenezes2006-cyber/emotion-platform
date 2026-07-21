#!/usr/bin/env python3
"""tDCS estimulação transcraniana info"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/tdcs", tags=["Tecnologia Saude"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "tDCS_info", "status": "ativo",
                          "descricao": "tDCS estimulação transcraniana info",
                          "categoria": "tecnologia_saude",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "tDCS_info",
                          "descricao": "tDCS estimulação transcraniana info",
                          "categoria": "tecnologia_saude",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "tDCS_info"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
