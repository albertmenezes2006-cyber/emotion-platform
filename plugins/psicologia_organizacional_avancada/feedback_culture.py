#!/usr/bin/env python3
"""Feedback Culture"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/feedback_culture", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_feedback_culture","s":"ativo","d":"Feedback Culture","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_feedback_culture"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
