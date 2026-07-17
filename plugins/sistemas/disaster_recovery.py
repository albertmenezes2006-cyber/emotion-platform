#!/usr/bin/env python3
"""Plano de recuperação"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/dr", tags=["Sistemas"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "disaster_recovery", "status": "ativo",
                          "descricao": "Plano de recuperação",
                          "versao": "1.0.0",
                          "categoria": "sistemas",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "disaster_recovery"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
