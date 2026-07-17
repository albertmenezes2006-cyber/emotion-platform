#!/usr/bin/env python3
"""Learning Organization"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/learning_organization", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_learning_organization","s":"ativo","d":"Learning Organization","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_learning_organization"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
