#!/usr/bin/env python3
"""Cultural Competence Emergency"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/cultural_competence_emergenc", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_cultural_competence_emerg","s":"ativo","d":"Cultural Competence Emergency","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_cultural_competence_emerg"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
