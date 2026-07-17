#!/usr/bin/env python3
"""Personnel Psychology"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/personnel_psychology", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_personnel_psychology","s":"ativo","d":"Personnel Psychology","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_personnel_psychology"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
