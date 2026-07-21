#!/usr/bin/env python3
"""Gestão do tempo de tela"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/tempo-tela", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "screen_time_management", "status": "ativo",
                          "descricao": "Gestão do tempo de tela",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "screen_time_management",
                          "descricao": "Gestão do tempo de tela",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "screen_time_management"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
