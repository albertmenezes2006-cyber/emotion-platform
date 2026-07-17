#!/usr/bin/env python3
"""Night Eating Vs Binge"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/night_eating_vs_binge", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_night_eating_vs_binge","s":"ativo","d":"Night Eating Vs Binge","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_night_eating_vs_binge"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
