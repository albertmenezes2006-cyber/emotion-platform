#!/usr/bin/env python3
"""Harassment Military"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/harassment_military", tags=["saude_mental_militar"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_milit_harassment_military","s":"ativo","d":"Harassment Military","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_milit_harassment_military"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
