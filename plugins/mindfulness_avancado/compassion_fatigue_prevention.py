#!/usr/bin/env python3
"""Compassion Fatigue Prevention"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/compassion_fatigue_preventio", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_compassion_fatigue_preven","s":"ativo","d":"Compassion Fatigue Prevention","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_compassion_fatigue_preven"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
