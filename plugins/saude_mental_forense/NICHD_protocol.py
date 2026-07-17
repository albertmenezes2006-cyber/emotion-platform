#!/usr/bin/env python3
"""Nichd Protocol"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/NICHD_protocol", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_NICHD_protocol","s":"ativo","d":"Nichd Protocol","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_NICHD_protocol"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
