#!/usr/bin/env python3
"""School Based Prevention"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/school_based_prevention", tags=["saude_mental_adolescencia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_adole_school_based_prevention","s":"ativo","d":"School Based Prevention","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_adole_school_based_prevention"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
