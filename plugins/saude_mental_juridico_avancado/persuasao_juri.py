#!/usr/bin/env python3
"""Persuasao Juri"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/persuasao_juri", tags=["saude_mental_juridico_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_jurid_persuasao_juri","s":"ativo","d":"Persuasao Juri","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_jurid_persuasao_juri"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
