#!/usr/bin/env python3
"""Oxitocina Social em saude integrativa"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/saude_integrati/oxitocina_social", tags=["saude_integrativa"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "saude_integrativa_oxitocina_social", "status": "ativo",
                          "descricao": "Oxitocina Social em saude integrativa", "categoria": "saude_integrativa",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "saude_integrativa_oxitocina_social"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
