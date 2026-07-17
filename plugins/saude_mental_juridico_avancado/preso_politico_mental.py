#!/usr/bin/env python3
"""Preso Politico Mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/preso_politico_mental", tags=["saude_mental_juridico_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_jurid_preso_politico_mental","s":"ativo","d":"Preso Politico Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_jurid_preso_politico_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
