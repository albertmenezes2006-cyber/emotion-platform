#!/usr/bin/env python3
"""Autoajuda guiada digital"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/autoajuda-guiada", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "guided_self_help", "status": "ativo",
                          "descricao": "Autoajuda guiada digital",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "guided_self_help",
                          "descricao": "Autoajuda guiada digital",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "guided_self_help"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
