#!/usr/bin/env python3
"""Moral Injury2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/moral_injury2", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_moral_injury2","s":"ativo","d":"Moral Injury2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_moral_injury2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
