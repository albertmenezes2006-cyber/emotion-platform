#!/usr/bin/env python3
"""Social Media Anxiety"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/social_media_anxiety", tags=["saude_mental_midia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_midia_social_media_anxiety","s":"ativo","d":"Social Media Anxiety","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_midia_social_media_anxiety"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
