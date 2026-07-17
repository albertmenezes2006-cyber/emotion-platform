#!/usr/bin/env python3
"""Decision Fatigue Emergency"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/decision_fatigue_emergency", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_decision_fatigue_emergenc","s":"ativo","d":"Decision Fatigue Emergency","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_decision_fatigue_emergenc"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
