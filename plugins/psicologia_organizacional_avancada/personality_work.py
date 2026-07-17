#!/usr/bin/env python3
"""Personality Work"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/personality_work", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_personality_work","s":"ativo","d":"Personality Work","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_personality_work"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
