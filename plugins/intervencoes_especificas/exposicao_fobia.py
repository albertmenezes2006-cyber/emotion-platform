#!/usr/bin/env python3
"""Exposicao Fobia em intervencoes especificas"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/intervencoes_es/exposicao_fobia", tags=["intervencoes_especificas"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"intervencoes_especif_exposicao_fobia","status":"ativo","desc":"Exposicao Fobia em intervencoes especificas","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "intervencoes_especif_exposicao_fobia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
