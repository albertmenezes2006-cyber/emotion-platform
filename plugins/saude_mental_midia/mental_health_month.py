#!/usr/bin/env python3
"""Mental Health Month"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/mental_health_month", tags=["saude_mental_midia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_midia_mental_health_month","s":"ativo","d":"Mental Health Month","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_midia_mental_health_month"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
