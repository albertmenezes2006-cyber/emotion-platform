#!/usr/bin/env python3
"""Open Space Technology"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/open_space_technology", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_open_space_technology","s":"ativo","d":"Open Space Technology","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_open_space_technology"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
