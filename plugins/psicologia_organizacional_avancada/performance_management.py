#!/usr/bin/env python3
"""Performance Management"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/performance_management", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_performance_management","s":"ativo","d":"Performance Management","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_performance_management"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
