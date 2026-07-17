#!/usr/bin/env python3
"""Open Questions Mindful"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/open_questions_mindful", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_open_questions_mindful","s":"ativo","d":"Open Questions Mindful","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_open_questions_mindful"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
