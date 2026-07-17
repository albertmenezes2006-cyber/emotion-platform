#!/usr/bin/env python3
"""Dialectical Behavior Mindful"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/dialectical_behavior_mindful", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_dialectical_behavior_mind","s":"ativo","d":"Dialectical Behavior Mindful","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_dialectical_behavior_mind"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
