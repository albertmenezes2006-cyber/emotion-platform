#!/usr/bin/env python3
"""Time To Change"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/time_to_change", tags=["saude_mental_midia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_midia_time_to_change","s":"ativo","d":"Time To Change","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_midia_time_to_change"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
