#!/usr/bin/env python3
"""Coaching Organizational"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/coaching_organizational", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_coaching_organizational","s":"ativo","d":"Coaching Organizational","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_coaching_organizational"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
