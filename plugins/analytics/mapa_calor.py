#!/usr/bin/env python3
"""Dados de mapa de calor"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/heatmap-data", tags=["mapa_calor"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "mapa_calor", "status": "ativo",
                          "descricao": "Dados de mapa de calor",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "mapa_calor"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
