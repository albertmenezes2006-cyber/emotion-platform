#!/usr/bin/env python3
"""Homelessness Veterans"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/homelessness_veterans", tags=["saude_mental_militar"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_milit_homelessness_veterans","s":"ativo","d":"Homelessness Veterans","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_milit_homelessness_veterans"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
