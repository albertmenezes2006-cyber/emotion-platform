#!/usr/bin/env python3
"""Critical Incident"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/critical_incident", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_critical_incident","s":"ativo","d":"Critical Incident","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_critical_incident"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
