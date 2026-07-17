#!/usr/bin/env python3
"""Advocacy em saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/advocacy", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "advocacy_mental_health", "status": "ativo",
                          "descricao": "Advocacy em saúde mental",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "advocacy_mental_health",
                          "descricao": "Advocacy em saúde mental",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "advocacy_mental_health"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
