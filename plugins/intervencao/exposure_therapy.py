#!/usr/bin/env python3
"""Protocolo de exposição gradual"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/exposicao-protocol", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "exposure_therapy", "status": "ativo",
                          "descricao": "Protocolo de exposição gradual",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "exposure_therapy",
                          "descricao": "Protocolo de exposição gradual",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "exposure_therapy"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
