#!/usr/bin/env python3
"""Restrictive Avoidant Vs Anorexia"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/restrictive_avoidant_vs_anor", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_restrictive_avoidant_vs_a","s":"ativo","d":"Restrictive Avoidant Vs Anorexia","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_restrictive_avoidant_vs_a"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
