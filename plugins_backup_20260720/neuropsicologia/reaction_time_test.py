#!/usr/bin/env python3
"""Tempo de reação digital"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/reaction-time", tags=["Neuropsicologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "reaction_time_test", "status": "ativo",
                          "descricao": "Tempo de reação digital",
                          "categoria": "neuropsicologia",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "reaction_time_test",
                          "descricao": "Tempo de reação digital",
                          "categoria": "neuropsicologia",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "reaction_time_test"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
