#!/usr/bin/env python3
"""Targeted Violence"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/targeted_violence", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_targeted_violence","s":"ativo","d":"Targeted Violence","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_targeted_violence"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
