#!/usr/bin/env python3
"""Terapia assistida por animais"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/animais", tags=["Natureza"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "animais_terapia", "status": "ativo",
                          "descricao": "Terapia assistida por animais",
                          "versao": "1.0.0",
                          "categoria": "natureza",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "animais_terapia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
