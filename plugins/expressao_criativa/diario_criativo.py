#!/usr/bin/env python3
"""Diario Criativo em expressao criativa"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/expressao_criat/diario_criativo", tags=["expressao_criativa"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "expressao_criativa_diario_criativo", "status": "ativo",
                          "descricao": "Diario Criativo em expressao criativa", "categoria": "expressao_criativa",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "expressao_criativa_diario_criativo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
