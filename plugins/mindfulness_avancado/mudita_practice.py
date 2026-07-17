#!/usr/bin/env python3
"""Mudita Practice"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/mudita_practice", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_mudita_practice","s":"ativo","d":"Mudita Practice","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_mudita_practice"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
