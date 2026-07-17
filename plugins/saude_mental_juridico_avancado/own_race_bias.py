#!/usr/bin/env python3
"""Own Race Bias"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/own_race_bias", tags=["saude_mental_juridico_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_jurid_own_race_bias","s":"ativo","d":"Own Race Bias","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_jurid_own_race_bias"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
