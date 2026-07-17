#!/usr/bin/env python3
"""World Cafe"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/world_cafe", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_world_cafe","s":"ativo","d":"World Cafe","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_world_cafe"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
