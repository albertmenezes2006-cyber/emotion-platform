#!/usr/bin/env python3
"""Cera Abelha em saude integrativa"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/saude_integrati/cera_abelha", tags=["saude_integrativa"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "saude_integrativa_cera_abelha", "status": "ativo",
                          "descricao": "Cera Abelha em saude integrativa", "categoria": "saude_integrativa",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "saude_integrativa_cera_abelha"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
