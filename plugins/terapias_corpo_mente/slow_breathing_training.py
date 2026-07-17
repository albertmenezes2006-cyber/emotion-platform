#!/usr/bin/env python3
"""Slow Breathing Training"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapias_cor/slow_breathing_training", tags=["terapias_corpo_mente"])
@router.get("")
async def info():
    return JSONResponse({"p":"terapias_corpo_men_slow_breathing_training","s":"ativo","d":"Slow Breathing Training","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapias_corpo_men_slow_breathing_training"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
