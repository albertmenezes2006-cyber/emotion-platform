#!/usr/bin/env python3
"""Mental Health Awareness"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/mental_health_awareness", tags=["saude_mental_midia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_midia_mental_health_awareness","s":"ativo","d":"Mental Health Awareness","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_midia_mental_health_awareness"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
