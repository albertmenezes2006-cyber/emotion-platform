#!/usr/bin/env python3
"""Efetividade Servico em saude coletiva mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_coletiva_/efetividade_servico", tags=["saude_coletiva_mental"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"saude_coletiva_menta_efetividade_servico","status":"ativo","desc":"Efetividade Servico em saude coletiva mental","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_coletiva_menta_efetividade_servico"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
