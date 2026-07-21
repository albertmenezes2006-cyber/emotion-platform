#!/usr/bin/env python3
"""Protocolo CBT para pânico"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/cbt-panico", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "cbt_panic_protocol", "status": "ativo",
                          "descricao": "Protocolo CBT para pânico",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "cbt_panic_protocol",
                          "descricao": "Protocolo CBT para pânico",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "cbt_panic_protocol"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
