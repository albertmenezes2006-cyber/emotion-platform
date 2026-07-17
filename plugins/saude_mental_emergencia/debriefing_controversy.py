#!/usr/bin/env python3
"""Debriefing Controversy"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/debriefing_controversy", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_debriefing_controversy","s":"ativo","d":"Debriefing Controversy","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_debriefing_controversy"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
