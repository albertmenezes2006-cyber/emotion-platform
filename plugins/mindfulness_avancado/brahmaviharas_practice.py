#!/usr/bin/env python3
"""Brahmaviharas Practice"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/brahmaviharas_practice", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_brahmaviharas_practice","s":"ativo","d":"Brahmaviharas Practice","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_brahmaviharas_practice"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
