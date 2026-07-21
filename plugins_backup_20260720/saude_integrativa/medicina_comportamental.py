#!/usr/bin/env python3
"""Medicina Comportamental em saude integrativa"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/saude_integrati/medicina_comportamental", tags=["saude_integrativa"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "saude_integrativa_medicina_comportamental", "status": "ativo",
                          "descricao": "Medicina Comportamental em saude integrativa", "categoria": "saude_integrativa",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "saude_integrativa_medicina_comportamental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
