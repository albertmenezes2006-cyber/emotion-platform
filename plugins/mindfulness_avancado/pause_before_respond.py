#!/usr/bin/env python3
"""Pause Before Respond"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/pause_before_respond", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_pause_before_respond","s":"ativo","d":"Pause Before Respond","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_pause_before_respond"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
