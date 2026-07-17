#!/usr/bin/env python3
"""Emotion Knowledge"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/emotion_knowledge", tags=["saude_mental_infancia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_infan_emotion_knowledge","s":"ativo","d":"Emotion Knowledge","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_infan_emotion_knowledge"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
