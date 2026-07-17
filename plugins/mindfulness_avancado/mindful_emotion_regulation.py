#!/usr/bin/env python3
"""Mindful Emotion Regulation"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/mindful_emotion_regulation", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_mindful_emotion_regulatio","s":"ativo","d":"Mindful Emotion Regulation","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_mindful_emotion_regulatio"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
