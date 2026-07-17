#!/usr/bin/env python3
"""Trauma Informed Emergency"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/trauma_informed_emergency", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_trauma_informed_emergency","s":"ativo","d":"Trauma Informed Emergency","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_trauma_informed_emergency"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
