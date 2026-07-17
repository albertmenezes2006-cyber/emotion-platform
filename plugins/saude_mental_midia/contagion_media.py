#!/usr/bin/env python3
"""Contagion Media"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/contagion_media", tags=["saude_mental_midia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_midia_contagion_media","s":"ativo","d":"Contagion Media","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_midia_contagion_media"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
