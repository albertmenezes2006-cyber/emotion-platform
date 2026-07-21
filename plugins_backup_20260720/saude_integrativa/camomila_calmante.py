#!/usr/bin/env python3
"""Camomila Calmante em saude integrativa"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/saude_integrati/camomila_calmante", tags=["saude_integrativa"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "saude_integrativa_camomila_calmante", "status": "ativo",
                          "descricao": "Camomila Calmante em saude integrativa", "categoria": "saude_integrativa",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "saude_integrativa_camomila_calmante"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
