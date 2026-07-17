#!/usr/bin/env python3
"""Pos Tortura"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/pos_tortura", tags=["saude_mental_juridico_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_jurid_pos_tortura","s":"ativo","d":"Pos Tortura","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_jurid_pos_tortura"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
