#!/usr/bin/env python3
"""Cognitively Based Compassion"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/cognitively_based_compassion", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_cognitively_based_compass","s":"ativo","d":"Cognitively Based Compassion","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_cognitively_based_compass"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
