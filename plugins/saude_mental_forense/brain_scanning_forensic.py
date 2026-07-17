#!/usr/bin/env python3
"""Brain Scanning Forensic"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/brain_scanning_forensic", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_brain_scanning_forensic","s":"ativo","d":"Brain Scanning Forensic","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_brain_scanning_forensic"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
