#!/usr/bin/env python3
"""Attentional Style"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/attentional_style", tags=["saude_mental_esporte"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_espor_attentional_style","s":"ativo","d":"Attentional Style","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_espor_attentional_style"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
