#!/usr/bin/env python3
"""Medicina Centrada Pessoa em saude integrativa"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/saude_integrati/medicina_centrada_pessoa", tags=["saude_integrativa"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "saude_integrativa_medicina_centrada_pessoa", "status": "ativo",
                          "descricao": "Medicina Centrada Pessoa em saude integrativa", "categoria": "saude_integrativa",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "saude_integrativa_medicina_centrada_pessoa"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
