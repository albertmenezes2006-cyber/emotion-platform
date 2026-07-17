#!/usr/bin/env python3
"""Luto Cultural2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/luto_cultural2", tags=["saude_mental_juridico_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_jurid_luto_cultural2","s":"ativo","d":"Luto Cultural2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_jurid_luto_cultural2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
