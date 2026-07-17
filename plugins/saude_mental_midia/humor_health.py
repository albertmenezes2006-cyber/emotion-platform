#!/usr/bin/env python3
"""Humor Health"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/humor_health", tags=["saude_mental_midia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_midia_humor_health","s":"ativo","d":"Humor Health","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_midia_humor_health"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
