#!/usr/bin/env python3
"""Victim Psychology"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/victim_psychology", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_victim_psychology","s":"ativo","d":"Victim Psychology","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_victim_psychology"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
