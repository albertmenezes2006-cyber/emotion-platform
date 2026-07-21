#!/usr/bin/env python3
"""EMDR protocolo 8 fases"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/emdr-fases", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "emdr_phase_protocol", "status": "ativo",
                          "descricao": "EMDR protocolo 8 fases",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "emdr_phase_protocol",
                          "descricao": "EMDR protocolo 8 fases",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "emdr_phase_protocol"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
