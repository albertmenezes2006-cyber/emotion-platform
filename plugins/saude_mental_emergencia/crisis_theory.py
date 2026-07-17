#!/usr/bin/env python3
"""Crisis Theory"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/crisis_theory", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_crisis_theory","s":"ativo","d":"Crisis Theory","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_crisis_theory"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
