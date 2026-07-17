#!/usr/bin/env python3
"""Liberating Structures"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/liberating_structures", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_liberating_structures","s":"ativo","d":"Liberating Structures","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_liberating_structures"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
