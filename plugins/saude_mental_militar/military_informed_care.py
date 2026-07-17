#!/usr/bin/env python3
"""Military Informed Care"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/military_informed_care", tags=["saude_mental_militar"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_milit_military_informed_care","s":"ativo","d":"Military Informed Care","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_milit_military_informed_care"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
