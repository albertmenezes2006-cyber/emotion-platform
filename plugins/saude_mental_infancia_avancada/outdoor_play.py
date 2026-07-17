#!/usr/bin/env python3
"""Outdoor Play"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/outdoor_play", tags=["saude_mental_infancia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_infan_outdoor_play","s":"ativo","d":"Outdoor Play","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_infan_outdoor_play"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
