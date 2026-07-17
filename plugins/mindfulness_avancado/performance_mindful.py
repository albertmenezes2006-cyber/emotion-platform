#!/usr/bin/env python3
"""Performance Mindful"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/performance_mindful", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_performance_mindful","s":"ativo","d":"Performance Mindful","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_performance_mindful"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
