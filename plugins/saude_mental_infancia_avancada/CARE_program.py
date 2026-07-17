#!/usr/bin/env python3
"""Care Program"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/CARE_program", tags=["saude_mental_infancia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_infan_CARE_program","s":"ativo","d":"Care Program","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_infan_CARE_program"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
