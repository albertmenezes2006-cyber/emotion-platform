#!/usr/bin/env python3
"""Tcc Abuso Substancia em intervencoes especificas"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/intervencoes_es/tcc_abuso_substancia", tags=["intervencoes_especificas"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"intervencoes_especif_tcc_abuso_substancia","status":"ativo","desc":"Tcc Abuso Substancia em intervencoes especificas","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "intervencoes_especif_tcc_abuso_substancia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
