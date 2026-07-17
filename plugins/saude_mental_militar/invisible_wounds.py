#!/usr/bin/env python3
"""Invisible Wounds"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/invisible_wounds", tags=["saude_mental_militar"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_milit_invisible_wounds","s":"ativo","d":"Invisible Wounds","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_milit_invisible_wounds"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
