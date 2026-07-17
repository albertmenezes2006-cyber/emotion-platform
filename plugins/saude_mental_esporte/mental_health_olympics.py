#!/usr/bin/env python3
"""Mental Health Olympics"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/mental_health_olympics", tags=["saude_mental_esporte"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_espor_mental_health_olympics","s":"ativo","d":"Mental Health Olympics","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_espor_mental_health_olympics"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
