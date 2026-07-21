#!/usr/bin/env python3
"""Folclore Terapia em expressao criativa"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/expressao_criat/folclore_terapia", tags=["expressao_criativa"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "expressao_criativa_folclore_terapia", "status": "ativo",
                          "descricao": "Folclore Terapia em expressao criativa", "categoria": "expressao_criativa",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "expressao_criativa_folclore_terapia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
