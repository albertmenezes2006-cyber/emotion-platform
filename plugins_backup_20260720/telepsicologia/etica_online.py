#!/usr/bin/env python3
"""Ética na psicologia online"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/etica-online", tags=["Telepsicologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "etica_online_psi", "status": "ativo",
                          "descricao": "Ética na psicologia online",
                          "versao": "1.0.0",
                          "categoria": "telepsicologia",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "etica_online_psi"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
