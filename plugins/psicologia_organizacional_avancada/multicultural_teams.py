#!/usr/bin/env python3
"""Multicultural Teams"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/multicultural_teams", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_multicultural_teams","s":"ativo","d":"Multicultural Teams","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_multicultural_teams"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
