#!/usr/bin/env python3
"""Gifted Teen Mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/gifted_teen_mental", tags=["saude_mental_adolescencia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_adole_gifted_teen_mental","s":"ativo","d":"Gifted Teen Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_adole_gifted_teen_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
