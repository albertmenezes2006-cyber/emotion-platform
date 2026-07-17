#!/usr/bin/env python3
"""Involuntary Commitment2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/involuntary_commitment2", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_involuntary_commitment2","s":"ativo","d":"Involuntary Commitment2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_involuntary_commitment2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
