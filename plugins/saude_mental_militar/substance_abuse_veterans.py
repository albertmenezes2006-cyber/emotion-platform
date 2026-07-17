#!/usr/bin/env python3
"""Substance Abuse Veterans"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/substance_abuse_veterans", tags=["saude_mental_militar"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_milit_substance_abuse_veterans","s":"ativo","d":"Substance Abuse Veterans","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_milit_substance_abuse_veterans"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
