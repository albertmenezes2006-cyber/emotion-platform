#!/usr/bin/env python3
"""Alternate Nostril"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapias_cor/alternate_nostril", tags=["terapias_corpo_mente"])
@router.get("")
async def info():
    return JSONResponse({"p":"terapias_corpo_men_alternate_nostril","s":"ativo","d":"Alternate Nostril","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapias_corpo_men_alternate_nostril"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
