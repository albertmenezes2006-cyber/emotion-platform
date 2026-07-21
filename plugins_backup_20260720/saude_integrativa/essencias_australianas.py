#!/usr/bin/env python3
"""Essencias Australianas em saude integrativa"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/saude_integrati/essencias_australianas", tags=["saude_integrativa"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "saude_integrativa_essencias_australianas", "status": "ativo",
                          "descricao": "Essencias Australianas em saude integrativa", "categoria": "saude_integrativa",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "saude_integrativa_essencias_australianas"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
