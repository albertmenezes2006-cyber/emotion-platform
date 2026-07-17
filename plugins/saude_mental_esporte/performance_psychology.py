#!/usr/bin/env python3
"""Performance Psychology"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/performance_psychology", tags=["saude_mental_esporte"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_espor_performance_psychology","s":"ativo","d":"Performance Psychology","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_espor_performance_psychology"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
