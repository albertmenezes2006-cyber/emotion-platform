#!/usr/bin/env python3
"""Physical Abuse Assessment"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/physical_abuse_assessment", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_physical_abuse_assessment","s":"ativo","d":"Physical Abuse Assessment","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_physical_abuse_assessment"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
