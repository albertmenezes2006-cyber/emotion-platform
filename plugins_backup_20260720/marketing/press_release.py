#!/usr/bin/env python3
"""Press release"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/press-release", tags=["press_release"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "press_release", "status": "ativo",
                          "descricao": "Press release",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "press_release"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
