#!/usr/bin/env python3
"""Combat Operational Stress"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/combat_operational_stress", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_combat_operational_stress","s":"ativo","d":"Combat Operational Stress","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_combat_operational_stress"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
