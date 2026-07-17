#!/usr/bin/env python3
"""Paramedic Mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/paramedic_mental", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_paramedic_mental","s":"ativo","d":"Paramedic Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_paramedic_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
