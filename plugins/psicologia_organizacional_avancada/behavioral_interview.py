#!/usr/bin/env python3
"""Behavioral Interview"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/behavioral_interview", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_behavioral_interview","s":"ativo","d":"Behavioral Interview","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_behavioral_interview"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
