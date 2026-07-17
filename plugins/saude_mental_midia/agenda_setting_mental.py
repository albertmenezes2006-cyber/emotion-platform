#!/usr/bin/env python3
"""Agenda Setting Mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/agenda_setting_mental", tags=["saude_mental_midia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_midia_agenda_setting_mental","s":"ativo","d":"Agenda Setting Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_midia_agenda_setting_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
