#!/usr/bin/env python3
"""Stress Inoculation Emergency"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/stress_inoculation_emergency", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_stress_inoculation_emerge","s":"ativo","d":"Stress Inoculation Emergency","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_stress_inoculation_emerge"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
