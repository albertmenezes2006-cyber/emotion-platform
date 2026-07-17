#!/usr/bin/env python3
"""Voice Prosody Therapy"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapias_cor/voice_prosody_therapy", tags=["terapias_corpo_mente"])
@router.get("")
async def info():
    return JSONResponse({"p":"terapias_corpo_men_voice_prosody_therapy","s":"ativo","d":"Voice Prosody Therapy","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapias_corpo_men_voice_prosody_therapy"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
