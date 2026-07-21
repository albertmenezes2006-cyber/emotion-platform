#!/usr/bin/env python3
"""Primeiros socorros em saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/psm", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "primeiros_socorros_mental", "status": "ativo",
                          "descricao": "Primeiros socorros em saúde mental",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "primeiros_socorros_mental",
                          "descricao": "Primeiros socorros em saúde mental",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "primeiros_socorros_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
