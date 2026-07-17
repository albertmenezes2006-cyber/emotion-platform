#!/usr/bin/env python3
"""Social Comparison Media"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/social_comparison_media", tags=["saude_mental_midia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_midia_social_comparison_media","s":"ativo","d":"Social Comparison Media","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_midia_social_comparison_media"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
