#!/usr/bin/env python3
"""Ujjayi Ocean"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapias_cor/ujjayi_ocean", tags=["terapias_corpo_mente"])
@router.get("")
async def info():
    return JSONResponse({"p":"terapias_corpo_men_ujjayi_ocean","s":"ativo","d":"Ujjayi Ocean","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapias_corpo_men_ujjayi_ocean"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
