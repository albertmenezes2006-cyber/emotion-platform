#!/usr/bin/env python3
"""Bijuteria Terapia em expressao criativa"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/expressao_criat/bijuteria_terapia", tags=["expressao_criativa"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "expressao_criativa_bijuteria_terapia", "status": "ativo",
                          "descricao": "Bijuteria Terapia em expressao criativa", "categoria": "expressao_criativa",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "expressao_criativa_bijuteria_terapia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
