#!/usr/bin/env python3
"""Calculadora de LTV"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/ltv", tags=["ltv_calc"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "ltv_calc", "status": "ativo",
                          "descricao": "Calculadora de LTV",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "ltv_calc"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
