#!/usr/bin/env python3
"""Trauma Migracao"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/trauma_migracao", tags=["saude_mental_juridico_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_jurid_trauma_migracao","s":"ativo","d":"Trauma Migracao","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_jurid_trauma_migracao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
