#!/usr/bin/env python3
"""Musicoterapia digital"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/musica", tags=["Musica Terapia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "musicoterapia", "status": "ativo",
                          "descricao": "Musicoterapia digital",
                          "versao": "1.0.0",
                          "categoria": "musica_terapia",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "musicoterapia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
