#!/usr/bin/env python3
"""Insanity Defense"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/insanity_defense", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_insanity_defense","s":"ativo","d":"Insanity Defense","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_insanity_defense"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
