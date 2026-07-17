#!/usr/bin/env python3
"""Papageno Effect2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/papageno_effect2", tags=["saude_mental_midia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_midia_papageno_effect2","s":"ativo","d":"Papageno Effect2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_midia_papageno_effect2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
