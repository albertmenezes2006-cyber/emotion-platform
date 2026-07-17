#!/usr/bin/env python3
"""Emdr Lite"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapias_cor/EMDR_lite", tags=["terapias_corpo_mente"])
@router.get("")
async def info():
    return JSONResponse({"p":"terapias_corpo_men_EMDR_lite","s":"ativo","d":"Emdr Lite","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapias_corpo_men_EMDR_lite"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
