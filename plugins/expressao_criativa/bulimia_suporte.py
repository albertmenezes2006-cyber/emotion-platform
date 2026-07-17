#!/usr/bin/env python3
"""Bulimia Suporte em expressao criativa"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/expressao_criat/bulimia_suporte", tags=["expressao_criativa"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "expressao_criativa_bulimia_suporte", "status": "ativo",
                          "descricao": "Bulimia Suporte em expressao criativa", "categoria": "expressao_criativa",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "expressao_criativa_bulimia_suporte"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
