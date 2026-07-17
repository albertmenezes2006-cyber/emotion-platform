#!/usr/bin/env python3
"""Bedside Manner Emergency"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/bedside_manner_emergency", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_bedside_manner_emergency","s":"ativo","d":"Bedside Manner Emergency","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_bedside_manner_emergency"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
