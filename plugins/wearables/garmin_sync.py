#!/usr/bin/env python3
"""Sync Garmin dados"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/garmin", tags=["Wearables"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "garmin_sync", "status": "ativo",
                          "descricao": "Sync Garmin dados",
                          "versao": "1.0.0",
                          "categoria": "wearables",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "garmin_sync"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
