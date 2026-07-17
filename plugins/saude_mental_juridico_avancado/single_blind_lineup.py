#!/usr/bin/env python3
"""Single Blind Lineup"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/single_blind_lineup", tags=["saude_mental_juridico_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_jurid_single_blind_lineup","s":"ativo","d":"Single Blind Lineup","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_jurid_single_blind_lineup"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
