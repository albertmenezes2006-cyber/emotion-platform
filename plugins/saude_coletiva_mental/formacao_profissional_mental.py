#!/usr/bin/env python3
"""Formacao Profissional Mental em saude coletiva mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_coletiva_/formacao_profissional_mental", tags=["saude_coletiva_mental"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"saude_coletiva_menta_formacao_profissional_men","status":"ativo","desc":"Formacao Profissional Mental em saude coletiva mental","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_coletiva_menta_formacao_profissional_men"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
