#!/usr/bin/env python3
"""Intimate Partner Emergency"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/intimate_partner_emergency", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_intimate_partner_emergenc","s":"ativo","d":"Intimate Partner Emergency","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_intimate_partner_emergenc"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
