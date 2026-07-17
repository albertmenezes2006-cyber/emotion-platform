#!/usr/bin/env python3
"""Pre Performance Routine"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/pre_performance_routine", tags=["saude_mental_esporte"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_espor_pre_performance_routine","s":"ativo","d":"Pre Performance Routine","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_espor_pre_performance_routine"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
