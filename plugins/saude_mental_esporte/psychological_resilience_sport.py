#!/usr/bin/env python3
"""Psychological Resilience Sport"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/psychological_resilience_spo", tags=["saude_mental_esporte"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_espor_psychological_resilience_","s":"ativo","d":"Psychological Resilience Sport","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_espor_psychological_resilience_"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
