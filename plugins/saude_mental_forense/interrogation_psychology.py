#!/usr/bin/env python3
"""Interrogation Psychology"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/interrogation_psychology", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_interrogation_psychology","s":"ativo","d":"Interrogation Psychology","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_interrogation_psychology"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
