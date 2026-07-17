#!/usr/bin/env python3
"""Orthorexia Vs Anorexia"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/orthorexia_vs_anorexia", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_orthorexia_vs_anorexia","s":"ativo","d":"Orthorexia Vs Anorexia","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_orthorexia_vs_anorexia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
