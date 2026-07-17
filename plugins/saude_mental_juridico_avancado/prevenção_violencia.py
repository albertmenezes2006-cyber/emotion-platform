#!/usr/bin/env python3
"""Prevenção Violencia"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/prevenção_violencia", tags=["saude_mental_juridico_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_jurid_prevenção_violencia","s":"ativo","d":"Prevenção Violencia","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_jurid_prevenção_violencia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
