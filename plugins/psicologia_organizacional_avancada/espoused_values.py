#!/usr/bin/env python3
"""Espoused Values"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/espoused_values", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_espoused_values","s":"ativo","d":"Espoused Values","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_espoused_values"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
