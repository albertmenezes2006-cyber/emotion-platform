#!/usr/bin/env python3
"""Avoidant Vs Social Anxiety"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/avoidant_vs_social_anxiety", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_avoidant_vs_social_anxiet","s":"ativo","d":"Avoidant Vs Social Anxiety","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_avoidant_vs_social_anxiet"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
