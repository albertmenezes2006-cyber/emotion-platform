#!/usr/bin/env python3
"""Rain Technique"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/RAIN_technique", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_RAIN_technique","s":"ativo","d":"Rain Technique","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_RAIN_technique"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
