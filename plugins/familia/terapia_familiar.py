#!/usr/bin/env python3
"""Recursos de terapia familiar"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/familia", tags=["Familia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "terapia_familiar", "status": "ativo",
                          "descricao": "Recursos de terapia familiar",
                          "versao": "1.0.0",
                          "categoria": "familia",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "terapia_familiar"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
