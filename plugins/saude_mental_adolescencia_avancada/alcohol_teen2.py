#!/usr/bin/env python3
"""Alcohol Teen2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/alcohol_teen2", tags=["saude_mental_adolescencia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_adole_alcohol_teen2","s":"ativo","d":"Alcohol Teen2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_adole_alcohol_teen2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
