#!/usr/bin/env python3
"""Copaiba Antiinfla em saude integrativa"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/saude_integrati/copaiba_antiinfla", tags=["saude_integrativa"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "saude_integrativa_copaiba_antiinfla", "status": "ativo",
                          "descricao": "Copaiba Antiinfla em saude integrativa", "categoria": "saude_integrativa",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "saude_integrativa_copaiba_antiinfla"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
