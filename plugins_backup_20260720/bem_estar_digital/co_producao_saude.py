#!/usr/bin/env python3
"""Co Producao Saude em bem estar digital"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/bem_estar_digit/co_producao_saude", tags=["bem_estar_digital"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "bem_estar_digital_co_producao_saude", "status": "ativo",
                          "descricao": "Co Producao Saude em bem estar digital", "categoria": "bem_estar_digital",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "bem_estar_digital_co_producao_saude"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
