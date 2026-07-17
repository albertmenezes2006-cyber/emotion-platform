#!/usr/bin/env python3
"""Shame Self Compassion"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/shame_self_compassion", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_shame_self_compassion","s":"ativo","d":"Shame Self Compassion","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_shame_self_compassion"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
