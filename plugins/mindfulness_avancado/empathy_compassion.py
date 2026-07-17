#!/usr/bin/env python3
"""Empathy Compassion"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/empathy_compassion", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_empathy_compassion","s":"ativo","d":"Empathy Compassion","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_empathy_compassion"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
