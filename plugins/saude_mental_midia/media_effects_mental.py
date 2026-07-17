#!/usr/bin/env python3
"""Media Effects Mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/media_effects_mental", tags=["saude_mental_midia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_midia_media_effects_mental","s":"ativo","d":"Media Effects Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_midia_media_effects_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
