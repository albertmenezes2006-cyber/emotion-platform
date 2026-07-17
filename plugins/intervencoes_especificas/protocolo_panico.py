#!/usr/bin/env python3
"""Protocolo Panico em intervencoes especificas"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/intervencoes_es/protocolo_panico", tags=["intervencoes_especificas"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"intervencoes_especif_protocolo_panico","status":"ativo","desc":"Protocolo Panico em intervencoes especificas","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "intervencoes_especif_protocolo_panico"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
