#!/usr/bin/env python3
"""Playlists terapêuticas por humor"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/playlist", tags=["Musica Terapia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "playlist_humor", "status": "ativo",
                          "descricao": "Playlists terapêuticas por humor",
                          "versao": "1.0.0",
                          "categoria": "musica_terapia",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "playlist_humor"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
