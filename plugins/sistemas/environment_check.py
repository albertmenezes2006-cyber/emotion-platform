#!/usr/bin/env python3
"""Verificação de variáveis"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/env-check", tags=["env_check"])

@router.get("")
async def info():
    return JSONResponse({"nome": "env_check", "status": "ativo",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "env_check"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
