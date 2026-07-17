#!/usr/bin/env python3
"""Contador regressivo"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/countdown", tags=["countdown_timer"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "countdown_timer", "status": "ativo",
                          "descricao": "Contador regressivo",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "countdown_timer"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
