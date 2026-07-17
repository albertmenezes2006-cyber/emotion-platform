#!/usr/bin/env python3
"""Wise Mind2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/wise_mind2", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_wise_mind2","s":"ativo","d":"Wise Mind2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_wise_mind2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
