#!/usr/bin/env python3
"""Msc Program"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/MSC_program", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_MSC_program","s":"ativo","d":"Msc Program","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_MSC_program"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
