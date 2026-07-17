#!/usr/bin/env python3
"""World Mental Health Day"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/world_mental_health_day", tags=["saude_mental_midia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_midia_world_mental_health_day","s":"ativo","d":"World Mental Health Day","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_midia_world_mental_health_day"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
