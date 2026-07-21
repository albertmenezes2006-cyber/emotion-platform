#!/usr/bin/env python3
"""Mídia e saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/midia-mental", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "media_influence_mental", "status": "ativo",
                          "descricao": "Mídia e saúde mental",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "media_influence_mental",
                          "descricao": "Mídia e saúde mental",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "media_influence_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
