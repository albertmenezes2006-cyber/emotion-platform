#!/usr/bin/env python3
"""Tcc Insonia2 em intervencoes especificas"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/intervencoes_es/tcc_insonia2", tags=["intervencoes_especificas"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"intervencoes_especif_tcc_insonia2","status":"ativo","desc":"Tcc Insonia2 em intervencoes especificas","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "intervencoes_especif_tcc_insonia2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
