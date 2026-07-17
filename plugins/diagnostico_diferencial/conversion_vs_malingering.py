#!/usr/bin/env python3
"""Conversion Vs Malingering"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/conversion_vs_malingering", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_conversion_vs_malingering","s":"ativo","d":"Conversion Vs Malingering","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_conversion_vs_malingering"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
