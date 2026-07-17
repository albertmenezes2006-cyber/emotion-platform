#!/usr/bin/env python3
"""Compassion Cultivation"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/compassion_cultivation", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_compassion_cultivation","s":"ativo","d":"Compassion Cultivation","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_compassion_cultivation"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
