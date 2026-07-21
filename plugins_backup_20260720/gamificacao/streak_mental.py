#!/usr/bin/env python3
"""Sistema de streak para saude mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/streak-mental", tags=["Essencial"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "streak_mental_adv", "status": "ativo",
                          "descricao": "Sistema de streak para saude mental",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "streak_mental_adv"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
