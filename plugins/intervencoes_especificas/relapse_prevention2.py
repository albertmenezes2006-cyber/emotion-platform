#!/usr/bin/env python3
"""Relapse Prevention2 em intervencoes especificas"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/intervencoes_es/relapse_prevention2", tags=["intervencoes_especificas"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"intervencoes_especif_relapse_prevention2","status":"ativo","desc":"Relapse Prevention2 em intervencoes especificas","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "intervencoes_especif_relapse_prevention2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
