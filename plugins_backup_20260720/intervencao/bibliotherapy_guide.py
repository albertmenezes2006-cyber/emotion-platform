#!/usr/bin/env python3
"""Biblioterapia guiada"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/biblioterapia", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "bibliotherapy_guide", "status": "ativo",
                          "descricao": "Biblioterapia guiada",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "bibliotherapy_guide",
                          "descricao": "Biblioterapia guiada",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "bibliotherapy_guide"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
