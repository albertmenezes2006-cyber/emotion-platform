#!/usr/bin/env python3
"""Saúde mental global"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/global-mental", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "global_mental_health", "status": "ativo",
                          "descricao": "Saúde mental global",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "global_mental_health",
                          "descricao": "Saúde mental global",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "global_mental_health"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
