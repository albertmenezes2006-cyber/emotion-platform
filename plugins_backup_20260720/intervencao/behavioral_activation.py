#!/usr/bin/env python3
"""Ativação comportamental protocolo"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/ba-protocol", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "behavioral_activation", "status": "ativo",
                          "descricao": "Ativação comportamental protocolo",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "behavioral_activation",
                          "descricao": "Ativação comportamental protocolo",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "behavioral_activation"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
