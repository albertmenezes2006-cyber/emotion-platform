#!/usr/bin/env python3
"""Winning Gracefully"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/winning_gracefully", tags=["saude_mental_infancia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_infan_winning_gracefully","s":"ativo","d":"Winning Gracefully","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_infan_winning_gracefully"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
