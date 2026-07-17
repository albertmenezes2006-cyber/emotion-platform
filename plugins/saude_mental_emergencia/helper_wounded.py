#!/usr/bin/env python3
"""Helper Wounded"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/helper_wounded", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_helper_wounded","s":"ativo","d":"Helper Wounded","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_helper_wounded"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
