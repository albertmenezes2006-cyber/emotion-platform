#!/usr/bin/env python3
"""Secondary Traumatic Stress2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/secondary_traumatic_stress2", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_secondary_traumatic_stres","s":"ativo","d":"Secondary Traumatic Stress2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_secondary_traumatic_stres"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
