#!/usr/bin/env python3
"""Emotional Intelligence Work"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/emotional_intelligence_work", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_emotional_intelligence_wo","s":"ativo","d":"Emotional Intelligence Work","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_emotional_intelligence_wo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
