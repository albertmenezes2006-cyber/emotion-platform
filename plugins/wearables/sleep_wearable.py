#!/usr/bin/env python3
"""Dados de sono de wearables"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/sleep-wear", tags=["Wearables"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "sleep_wearable", "status": "ativo",
                          "descricao": "Dados de sono de wearables",
                          "versao": "1.0.0",
                          "categoria": "wearables",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "sleep_wearable"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
