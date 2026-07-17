#!/usr/bin/env python3
"""Situational Interview"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/situational_interview", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_situational_interview","s":"ativo","d":"Situational Interview","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_situational_interview"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
