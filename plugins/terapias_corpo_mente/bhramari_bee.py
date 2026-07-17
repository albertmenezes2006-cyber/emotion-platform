#!/usr/bin/env python3
"""Bhramari Bee"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapias_cor/bhramari_bee", tags=["terapias_corpo_mente"])
@router.get("")
async def info():
    return JSONResponse({"p":"terapias_corpo_men_bhramari_bee","s":"ativo","d":"Bhramari Bee","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapias_corpo_men_bhramari_bee"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
