#!/usr/bin/env python3
"""Organizational Change"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/organizational_change", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_organizational_change","s":"ativo","d":"Organizational Change","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_organizational_change"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
