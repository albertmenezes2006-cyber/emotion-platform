#!/usr/bin/env python3
"""Medicina 4P Saude em saude integrativa"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/saude_integrati/medicina_4p_saude", tags=["saude_integrativa"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "saude_integrativa_medicina_4p_saude", "status": "ativo",
                          "descricao": "Medicina 4P Saude em saude integrativa", "categoria": "saude_integrativa",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "saude_integrativa_medicina_4p_saude"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
