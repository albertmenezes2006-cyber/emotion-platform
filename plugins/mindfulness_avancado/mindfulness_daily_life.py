#!/usr/bin/env python3
"""Mindfulness Daily Life"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/mindfulness_daily_life", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_mindfulness_daily_life","s":"ativo","d":"Mindfulness Daily Life","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_mindfulness_daily_life"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
