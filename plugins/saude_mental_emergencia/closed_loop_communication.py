#!/usr/bin/env python3
"""Closed Loop Communication"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/closed_loop_communication", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_closed_loop_communication","s":"ativo","d":"Closed Loop Communication","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_closed_loop_communication"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
