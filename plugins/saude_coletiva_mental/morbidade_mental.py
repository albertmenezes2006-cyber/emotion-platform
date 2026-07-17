#!/usr/bin/env python3
"""Morbidade Mental em saude coletiva mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_coletiva_/morbidade_mental", tags=["saude_coletiva_mental"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"saude_coletiva_menta_morbidade_mental","status":"ativo","desc":"Morbidade Mental em saude coletiva mental","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_coletiva_menta_morbidade_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
