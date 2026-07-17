#!/usr/bin/env python3
"""Community Violence"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/community_violence", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_community_violence","s":"ativo","d":"Community Violence","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_community_violence"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
