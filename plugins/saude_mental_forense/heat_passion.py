#!/usr/bin/env python3
"""Heat Passion"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/heat_passion", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_heat_passion","s":"ativo","d":"Heat Passion","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_heat_passion"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
