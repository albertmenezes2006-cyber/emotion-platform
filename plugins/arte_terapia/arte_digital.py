#!/usr/bin/env python3
"""Arteterapia digital"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/arte", tags=["Arte Terapia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "arte_digital_terapia", "status": "ativo",
                          "descricao": "Arteterapia digital",
                          "versao": "1.0.0",
                          "categoria": "arte_terapia",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "arte_digital_terapia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
