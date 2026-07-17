#!/usr/bin/env python3
"""Interoceptive Awareness"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapias_cor/interoceptive_awareness", tags=["terapias_corpo_mente"])
@router.get("")
async def info():
    return JSONResponse({"p":"terapias_corpo_men_interoceptive_awareness","s":"ativo","d":"Interoceptive Awareness","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapias_corpo_men_interoceptive_awareness"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
