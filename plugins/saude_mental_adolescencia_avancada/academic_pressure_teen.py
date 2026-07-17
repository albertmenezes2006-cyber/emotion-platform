#!/usr/bin/env python3
"""Academic Pressure Teen"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/academic_pressure_teen", tags=["saude_mental_adolescencia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_adole_academic_pressure_teen","s":"ativo","d":"Academic Pressure Teen","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_adole_academic_pressure_teen"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
