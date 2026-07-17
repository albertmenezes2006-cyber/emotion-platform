#!/usr/bin/env python3
"""Binaural beats para relaxamento"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/binaural", tags=["Musica Terapia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "binaural_beats", "status": "ativo",
                          "descricao": "Binaural beats para relaxamento",
                          "versao": "1.0.0",
                          "categoria": "musica_terapia",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "binaural_beats"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
