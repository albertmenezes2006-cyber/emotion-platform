#!/usr/bin/env python3
"""Detox digital programado"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/detox-digital", tags=["Adicoes"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "digital_detox", "status": "ativo",
                          "descricao": "Detox digital programado",
                          "versao": "1.0.0",
                          "categoria": "adicoes",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "digital_detox"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
