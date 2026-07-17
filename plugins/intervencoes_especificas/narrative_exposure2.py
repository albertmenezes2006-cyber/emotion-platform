#!/usr/bin/env python3
"""Narrative Exposure2 em intervencoes especificas"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/intervencoes_es/narrative_exposure2", tags=["intervencoes_especificas"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"intervencoes_especif_narrative_exposure2","status":"ativo","desc":"Narrative Exposure2 em intervencoes especificas","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "intervencoes_especif_narrative_exposure2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
