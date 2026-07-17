#!/usr/bin/env python3
"""Belonging Work"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/belonging_work", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_belonging_work","s":"ativo","d":"Belonging Work","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_belonging_work"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
