#!/usr/bin/env python3
"""Heart Brain Coherence"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapias_cor/heart_brain_coherence", tags=["terapias_corpo_mente"])
@router.get("")
async def info():
    return JSONResponse({"p":"terapias_corpo_men_heart_brain_coherence","s":"ativo","d":"Heart Brain Coherence","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapias_corpo_men_heart_brain_coherence"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
