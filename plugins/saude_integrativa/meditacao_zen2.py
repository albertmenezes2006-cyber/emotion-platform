#!/usr/bin/env python3
"""Meditacao Zen2 em saude integrativa"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/saude_integrati/meditacao_zen2", tags=["saude_integrativa"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "saude_integrativa_meditacao_zen2", "status": "ativo",
                          "descricao": "Meditacao Zen2 em saude integrativa", "categoria": "saude_integrativa",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "saude_integrativa_meditacao_zen2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
