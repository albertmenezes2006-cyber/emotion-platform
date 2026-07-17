#!/usr/bin/env python3
"""Developmental Trauma"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/developmental_trauma", tags=["saude_mental_infancia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_infan_developmental_trauma","s":"ativo","d":"Developmental Trauma","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_infan_developmental_trauma"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
