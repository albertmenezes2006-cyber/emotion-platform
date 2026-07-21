#!/usr/bin/env python3
"""Sync Apple Watch dados de saúde"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/apple-watch", tags=["Wearables"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "apple_watch", "status": "ativo",
                          "descricao": "Sync Apple Watch dados de saúde",
                          "versao": "1.0.0",
                          "categoria": "wearables",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "apple_watch"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
