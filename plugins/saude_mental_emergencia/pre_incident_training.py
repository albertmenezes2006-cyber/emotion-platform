#!/usr/bin/env python3
"""Pre Incident Training"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/pre_incident_training", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_pre_incident_training","s":"ativo","d":"Pre Incident Training","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_pre_incident_training"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
