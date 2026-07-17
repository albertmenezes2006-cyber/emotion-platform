#!/usr/bin/env python3
"""Anorexia Vs Bulimia"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/anorexia_vs_bulimia", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_anorexia_vs_bulimia","s":"ativo","d":"Anorexia Vs Bulimia","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_anorexia_vs_bulimia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
