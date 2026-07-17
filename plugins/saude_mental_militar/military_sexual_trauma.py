#!/usr/bin/env python3
"""Military Sexual Trauma"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/military_sexual_trauma", tags=["saude_mental_militar"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_milit_military_sexual_trauma","s":"ativo","d":"Military Sexual Trauma","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_milit_military_sexual_trauma"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
