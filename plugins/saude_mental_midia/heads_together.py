#!/usr/bin/env python3
"""Heads Together"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/heads_together", tags=["saude_mental_midia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_midia_heads_together","s":"ativo","d":"Heads Together","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_midia_heads_together"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
