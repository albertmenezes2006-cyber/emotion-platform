#!/usr/bin/env python3
"""Empatia Emocional"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/empatia_emocional", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_empatia_emocional","s":"ativo","d":"Empatia Emocional","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_empatia_emocional"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
