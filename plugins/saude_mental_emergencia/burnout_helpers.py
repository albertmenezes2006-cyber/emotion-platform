#!/usr/bin/env python3
"""Burnout Helpers"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/burnout_helpers", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_burnout_helpers","s":"ativo","d":"Burnout Helpers","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_burnout_helpers"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
