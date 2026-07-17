#!/usr/bin/env python3
"""Fusos horários brasileiros"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/timezone", tags=["timezone_br"])

@router.get("")
async def info():
    return JSONResponse({"nome": "timezone_br", "status": "ativo",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "timezone_br"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
