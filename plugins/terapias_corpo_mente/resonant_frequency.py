#!/usr/bin/env python3
"""Resonant Frequency"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapias_cor/resonant_frequency", tags=["terapias_corpo_mente"])
@router.get("")
async def info():
    return JSONResponse({"p":"terapias_corpo_men_resonant_frequency","s":"ativo","d":"Resonant Frequency","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapias_corpo_men_resonant_frequency"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
