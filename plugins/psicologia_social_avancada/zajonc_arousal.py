#!/usr/bin/env python3
"""Zajonc Arousal"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/zajonc_arousal", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__zajonc_arousal","s":"ativo","d":"Zajonc Arousal","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__zajonc_arousal"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
