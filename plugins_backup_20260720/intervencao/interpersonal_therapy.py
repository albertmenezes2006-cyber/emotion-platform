#!/usr/bin/env python3
"""IPT protocolo interpessoal"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/ipt-protocol", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "interpersonal_therapy", "status": "ativo",
                          "descricao": "IPT protocolo interpessoal",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "interpersonal_therapy",
                          "descricao": "IPT protocolo interpessoal",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "interpersonal_therapy"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
