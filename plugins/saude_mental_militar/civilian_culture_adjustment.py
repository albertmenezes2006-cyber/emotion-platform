#!/usr/bin/env python3
"""Civilian Culture Adjustment"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/civilian_culture_adjustment", tags=["saude_mental_militar"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_milit_civilian_culture_adjustme","s":"ativo","d":"Civilian Culture Adjustment","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_milit_civilian_culture_adjustme"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
