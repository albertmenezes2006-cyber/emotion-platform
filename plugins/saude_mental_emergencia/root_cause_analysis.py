#!/usr/bin/env python3
"""Root Cause Analysis"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/root_cause_analysis", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_root_cause_analysis","s":"ativo","d":"Root Cause Analysis","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_root_cause_analysis"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
