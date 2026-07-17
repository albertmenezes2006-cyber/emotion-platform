#!/usr/bin/env python3
"""Cue Words"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/cue_words", tags=["saude_mental_esporte"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_espor_cue_words","s":"ativo","d":"Cue Words","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_espor_cue_words"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
