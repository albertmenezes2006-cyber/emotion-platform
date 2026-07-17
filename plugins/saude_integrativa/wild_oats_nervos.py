#!/usr/bin/env python3
"""Wild Oats Nervos em saude integrativa"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/saude_integrati/wild_oats_nervos", tags=["saude_integrativa"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "saude_integrativa_wild_oats_nervos", "status": "ativo",
                          "descricao": "Wild Oats Nervos em saude integrativa", "categoria": "saude_integrativa",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "saude_integrativa_wild_oats_nervos"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
