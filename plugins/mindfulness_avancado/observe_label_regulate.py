#!/usr/bin/env python3
"""Observe Label Regulate"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/observe_label_regulate", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_observe_label_regulate","s":"ativo","d":"Observe Label Regulate","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_observe_label_regulate"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
