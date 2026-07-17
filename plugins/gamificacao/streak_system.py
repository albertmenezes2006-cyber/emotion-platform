#!/usr/bin/env python3
"""Sistema de streak avançado"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/streak", tags=["Gamificacao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "streak_system_adv", "status": "ativo",
                          "descricao": "Sistema de streak avançado",
                          "versao": "1.0.0",
                          "categoria": "gamificacao",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "streak_system_adv"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
