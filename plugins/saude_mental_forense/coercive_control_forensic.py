#!/usr/bin/env python3
"""Coercive Control Forensic"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/coercive_control_forensic", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_coercive_control_forensic","s":"ativo","d":"Coercive Control Forensic","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_coercive_control_forensic"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
