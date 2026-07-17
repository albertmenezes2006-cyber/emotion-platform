#!/usr/bin/env python3
"""Tonglen Advanced"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/tonglen_advanced", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_tonglen_advanced","s":"ativo","d":"Tonglen Advanced","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_tonglen_advanced"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
