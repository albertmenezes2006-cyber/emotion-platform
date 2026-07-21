#!/usr/bin/env python3
"""Portabilidade Dados2 em bem estar digital"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/bem_estar_digit/portabilidade_dados2", tags=["bem_estar_digital"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "bem_estar_digital_portabilidade_dados2", "status": "ativo",
                          "descricao": "Portabilidade Dados2 em bem estar digital", "categoria": "bem_estar_digital",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "bem_estar_digital_portabilidade_dados2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
