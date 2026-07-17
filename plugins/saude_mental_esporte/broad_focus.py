#!/usr/bin/env python3
"""Broad Focus"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/broad_focus", tags=["saude_mental_esporte"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_espor_broad_focus","s":"ativo","d":"Broad Focus","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_espor_broad_focus"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
