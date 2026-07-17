#!/usr/bin/env python3
"""Civic Virtue"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/civic_virtue", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_civic_virtue","s":"ativo","d":"Civic Virtue","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_civic_virtue"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
