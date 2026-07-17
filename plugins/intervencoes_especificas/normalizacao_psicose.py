#!/usr/bin/env python3
"""Normalizacao Psicose em intervencoes especificas"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/intervencoes_es/normalizacao_psicose", tags=["intervencoes_especificas"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"intervencoes_especif_normalizacao_psicose","status":"ativo","desc":"Normalizacao Psicose em intervencoes especificas","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "intervencoes_especif_normalizacao_psicose"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
