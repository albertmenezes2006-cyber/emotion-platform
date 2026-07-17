#!/usr/bin/env python3
"""Biofeedback Hrv2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapias_cor/biofeedback_hrv2", tags=["terapias_corpo_mente"])
@router.get("")
async def info():
    return JSONResponse({"p":"terapias_corpo_men_biofeedback_hrv2","s":"ativo","d":"Biofeedback Hrv2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapias_corpo_men_biofeedback_hrv2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
