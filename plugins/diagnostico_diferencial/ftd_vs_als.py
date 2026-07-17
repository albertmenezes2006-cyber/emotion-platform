#!/usr/bin/env python3
"""Ftd Vs Als"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/ftd_vs_als", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_ftd_vs_als","s":"ativo","d":"Ftd Vs Als","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_ftd_vs_als"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
