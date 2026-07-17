#!/usr/bin/env python3
"""Sport Psychology Mindful"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/sport_psychology_mindful", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_sport_psychology_mindful","s":"ativo","d":"Sport Psychology Mindful","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_sport_psychology_mindful"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
