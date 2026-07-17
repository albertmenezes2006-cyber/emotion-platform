#!/usr/bin/env python3
"""Conversion Therapy Harm"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/conversion_therapy_harm", tags=["saude_mental_adolescencia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_adole_conversion_therapy_harm","s":"ativo","d":"Conversion Therapy Harm","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_adole_conversion_therapy_harm"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
