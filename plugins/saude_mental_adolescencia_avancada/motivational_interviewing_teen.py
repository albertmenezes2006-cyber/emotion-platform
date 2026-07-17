#!/usr/bin/env python3
"""Motivational Interviewing Teen"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/motivational_interviewing_te", tags=["saude_mental_adolescencia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_adole_motivational_interviewing","s":"ativo","d":"Motivational Interviewing Teen","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_adole_motivational_interviewing"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
