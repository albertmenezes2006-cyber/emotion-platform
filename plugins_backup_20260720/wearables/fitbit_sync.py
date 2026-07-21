#!/usr/bin/env python3
"""Sync Fitbit para saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/fitbit", tags=["Wearables"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "fitbit_sync", "status": "ativo",
                          "descricao": "Sync Fitbit para saúde mental",
                          "versao": "1.0.0",
                          "categoria": "wearables",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "fitbit_sync"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
