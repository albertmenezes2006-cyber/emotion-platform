#!/usr/bin/env python3
"""Polygraph Forensic"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/polygraph_forensic", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_polygraph_forensic","s":"ativo","d":"Polygraph Forensic","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_polygraph_forensic"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
