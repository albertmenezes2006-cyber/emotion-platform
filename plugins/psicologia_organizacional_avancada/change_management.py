#!/usr/bin/env python3
"""Change Management"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/change_management", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_change_management","s":"ativo","d":"Change Management","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_change_management"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
