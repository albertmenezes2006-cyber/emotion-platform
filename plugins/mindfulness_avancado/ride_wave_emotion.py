#!/usr/bin/env python3
"""Ride Wave Emotion"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/ride_wave_emotion", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_ride_wave_emotion","s":"ativo","d":"Ride Wave Emotion","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_ride_wave_emotion"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
