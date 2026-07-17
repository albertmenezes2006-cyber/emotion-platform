#!/usr/bin/env python3
"""Ocd Personality Vs Ocd"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/ocd_personality_vs_ocd", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_ocd_personality_vs_ocd","s":"ativo","d":"Ocd Personality Vs Ocd","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_ocd_personality_vs_ocd"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
