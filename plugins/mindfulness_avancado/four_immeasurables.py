#!/usr/bin/env python3
"""Four Immeasurables"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/four_immeasurables", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_four_immeasurables","s":"ativo","d":"Four Immeasurables","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_four_immeasurables"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
