#!/usr/bin/env python3
"""Executive Coaching"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/executive_coaching", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_executive_coaching","s":"ativo","d":"Executive Coaching","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_executive_coaching"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
