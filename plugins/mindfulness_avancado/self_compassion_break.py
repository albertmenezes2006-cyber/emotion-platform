#!/usr/bin/env python3
"""Self Compassion Break"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/self_compassion_break", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_self_compassion_break","s":"ativo","d":"Self Compassion Break","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_self_compassion_break"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
