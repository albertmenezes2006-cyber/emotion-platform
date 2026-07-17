#!/usr/bin/env python3
"""Social Media Depression"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/social_media_depression", tags=["saude_mental_midia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_midia_social_media_depression","s":"ativo","d":"Social Media Depression","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_midia_social_media_depression"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
