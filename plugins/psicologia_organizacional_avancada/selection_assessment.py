#!/usr/bin/env python3
"""Selection Assessment"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/selection_assessment", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_selection_assessment","s":"ativo","d":"Selection Assessment","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_selection_assessment"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
