#!/usr/bin/env python3
"""Adolescent Brain"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/adolescent_brain", tags=["saude_mental_adolescencia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_adole_adolescent_brain","s":"ativo","d":"Adolescent Brain","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_adole_adolescent_brain"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
