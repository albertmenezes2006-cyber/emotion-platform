#!/usr/bin/env python3
"""Epigenetics Early"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/epigenetics_early", tags=["saude_mental_infancia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_infan_epigenetics_early","s":"ativo","d":"Epigenetics Early","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_infan_epigenetics_early"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
