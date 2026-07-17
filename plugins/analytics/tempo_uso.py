#!/usr/bin/env python3
"""Análise tempo de uso"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/tempo-uso", tags=["tempo_uso"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "tempo_uso", "status": "ativo",
                          "descricao": "Análise tempo de uso",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "tempo_uso"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
