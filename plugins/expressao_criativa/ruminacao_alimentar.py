#!/usr/bin/env python3
"""Ruminacao Alimentar em expressao criativa"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/expressao_criat/ruminacao_alimentar", tags=["expressao_criativa"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "expressao_criativa_ruminacao_alimentar", "status": "ativo",
                          "descricao": "Ruminacao Alimentar em expressao criativa", "categoria": "expressao_criativa",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "expressao_criativa_ruminacao_alimentar"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
