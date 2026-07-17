#!/usr/bin/env python3
"""Sequential Lineup"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/sequential_lineup", tags=["saude_mental_juridico_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_jurid_sequential_lineup","s":"ativo","d":"Sequential Lineup","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_jurid_sequential_lineup"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
