#!/usr/bin/env python3
"""Bell Lets Talk"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/bell_lets_talk", tags=["saude_mental_midia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_midia_bell_lets_talk","s":"ativo","d":"Bell Lets Talk","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_midia_bell_lets_talk"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
