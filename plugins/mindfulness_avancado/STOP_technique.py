#!/usr/bin/env python3
"""Stop Technique"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/STOP_technique", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_STOP_technique","s":"ativo","d":"Stop Technique","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_STOP_technique"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
