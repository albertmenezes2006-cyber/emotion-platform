#!/usr/bin/env python3
"""Ritmo e percussão terapêutica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/ritmo", tags=["Musica Terapia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "ritmo_terapia", "status": "ativo",
                          "descricao": "Ritmo e percussão terapêutica",
                          "versao": "1.0.0",
                          "categoria": "musica_terapia",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "ritmo_terapia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
