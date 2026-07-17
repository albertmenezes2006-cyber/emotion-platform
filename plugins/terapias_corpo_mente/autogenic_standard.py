#!/usr/bin/env python3
"""Autogenic Standard"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapias_cor/autogenic_standard", tags=["terapias_corpo_mente"])
@router.get("")
async def info():
    return JSONResponse({"p":"terapias_corpo_men_autogenic_standard","s":"ativo","d":"Autogenic Standard","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapias_corpo_men_autogenic_standard"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
