#!/usr/bin/env python3
"""Post Incident Support"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/post_incident_support", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_post_incident_support","s":"ativo","d":"Post Incident Support","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_post_incident_support"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
