#!/usr/bin/env python3
"""Saúde mental comunitária"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/saude-comunidade", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "community_mental_health", "status": "ativo",
                          "descricao": "Saúde mental comunitária",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "community_mental_health",
                          "descricao": "Saúde mental comunitária",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "community_mental_health"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
