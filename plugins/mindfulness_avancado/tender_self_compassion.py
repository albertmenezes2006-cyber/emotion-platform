#!/usr/bin/env python3
"""Tender Self Compassion"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/tender_self_compassion", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_tender_self_compassion","s":"ativo","d":"Tender Self Compassion","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_tender_self_compassion"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
