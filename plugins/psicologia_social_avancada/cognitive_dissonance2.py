#!/usr/bin/env python3
"""Cognitive Dissonance2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/cognitive_dissonance2", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__cognitive_dissonance2","s":"ativo","d":"Cognitive Dissonance2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__cognitive_dissonance2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
