#!/usr/bin/env python3
"""Performance Climate"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/performance_climate", tags=["saude_mental_esporte"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_espor_performance_climate","s":"ativo","d":"Performance Climate","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_espor_performance_climate"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
