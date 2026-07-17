#!/usr/bin/env python3
"""Lineup Procedure"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/lineup_procedure", tags=["saude_mental_juridico_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_jurid_lineup_procedure","s":"ativo","d":"Lineup Procedure","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_jurid_lineup_procedure"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
