#!/usr/bin/env python3
"""Cams Protocol2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/CAMS_protocol2", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_CAMS_protocol2","s":"ativo","d":"Cams Protocol2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_CAMS_protocol2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
