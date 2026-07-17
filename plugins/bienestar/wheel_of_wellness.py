#!/usr/bin/env python3
"""Roda do bem-estar completa"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/wheel-wellness", tags=["Essencial"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "wheel_wellness", "status": "ativo",
                          "descricao": "Roda do bem-estar completa",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "wheel_wellness"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
