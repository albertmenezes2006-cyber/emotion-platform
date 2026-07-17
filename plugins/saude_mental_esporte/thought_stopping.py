#!/usr/bin/env python3
"""Thought Stopping"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/thought_stopping", tags=["saude_mental_esporte"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_espor_thought_stopping","s":"ativo","d":"Thought Stopping","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_espor_thought_stopping"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
