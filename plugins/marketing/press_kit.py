#!/usr/bin/env python3
"""Press kit para imprensa"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/press", tags=["press_kit"])

@router.get("")
async def info():
    return JSONResponse({"nome": "press_kit", "status": "ativo",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "press_kit"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
