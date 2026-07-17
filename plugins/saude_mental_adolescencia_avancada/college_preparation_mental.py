#!/usr/bin/env python3
"""College Preparation Mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/college_preparation_mental", tags=["saude_mental_adolescencia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_adole_college_preparation_menta","s":"ativo","d":"College Preparation Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_adole_college_preparation_menta"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
