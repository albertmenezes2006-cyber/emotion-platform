#!/usr/bin/env python3
"""Voice Behavior"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/voice_behavior", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_voice_behavior","s":"ativo","d":"Voice Behavior","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_voice_behavior"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
