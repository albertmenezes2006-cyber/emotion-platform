#!/usr/bin/env python3
"""Qualidade Servico em saude coletiva mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_coletiva_/qualidade_servico", tags=["saude_coletiva_mental"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"saude_coletiva_menta_qualidade_servico","status":"ativo","desc":"Qualidade Servico em saude coletiva mental","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_coletiva_menta_qualidade_servico"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
