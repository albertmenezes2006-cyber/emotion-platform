#!/usr/bin/env python3
"""Agentes Comunitarios em saude coletiva mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_coletiva_/agentes_comunitarios", tags=["saude_coletiva_mental"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"saude_coletiva_menta_agentes_comunitarios","status":"ativo","desc":"Agentes Comunitarios em saude coletiva mental","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_coletiva_menta_agentes_comunitarios"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
