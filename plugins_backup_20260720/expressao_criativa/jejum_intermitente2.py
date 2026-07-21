#!/usr/bin/env python3
"""Jejum Intermitente2 em expressao criativa"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/expressao_criat/jejum_intermitente2", tags=["expressao_criativa"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "expressao_criativa_jejum_intermitente2", "status": "ativo",
                          "descricao": "Jejum Intermitente2 em expressao criativa", "categoria": "expressao_criativa",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "expressao_criativa_jejum_intermitente2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
