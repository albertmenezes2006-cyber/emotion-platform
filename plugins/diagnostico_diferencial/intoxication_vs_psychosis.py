#!/usr/bin/env python3
"""Intoxication Vs Psychosis"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/intoxication_vs_psychosis", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_intoxication_vs_psychosis","s":"ativo","d":"Intoxication Vs Psychosis","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_intoxication_vs_psychosis"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
