#!/usr/bin/env python3
"""Threat Assessment"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/threat_assessment", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_threat_assessment","s":"ativo","d":"Threat Assessment","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_threat_assessment"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
