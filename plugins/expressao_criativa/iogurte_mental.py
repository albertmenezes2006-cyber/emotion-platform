#!/usr/bin/env python3
"""Iogurte Mental em expressao criativa"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/expressao_criat/iogurte_mental", tags=["expressao_criativa"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "expressao_criativa_iogurte_mental", "status": "ativo",
                          "descricao": "Iogurte Mental em expressao criativa", "categoria": "expressao_criativa",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "expressao_criativa_iogurte_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
