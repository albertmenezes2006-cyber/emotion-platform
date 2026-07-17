#!/usr/bin/env python3
"""Availability"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/availability", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__availability","s":"ativo","d":"Availability","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__availability"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
