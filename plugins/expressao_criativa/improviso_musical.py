#!/usr/bin/env python3
"""Improviso Musical em expressao criativa"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/expressao_criat/improviso_musical", tags=["expressao_criativa"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "expressao_criativa_improviso_musical", "status": "ativo",
                          "descricao": "Improviso Musical em expressao criativa", "categoria": "expressao_criativa",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "expressao_criativa_improviso_musical"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
