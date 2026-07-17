#!/usr/bin/env python3
"""Psychiatric Boarding"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/psychiatric_boarding", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_psychiatric_boarding","s":"ativo","d":"Psychiatric Boarding","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_psychiatric_boarding"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
