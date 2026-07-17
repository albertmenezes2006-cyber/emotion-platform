#!/usr/bin/env python3
"""Mindful Grief"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/mindful_grief", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_mindful_grief","s":"ativo","d":"Mindful Grief","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_mindful_grief"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
