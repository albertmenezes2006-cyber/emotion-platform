#!/usr/bin/env python3
"""Gender Affirming"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/gender_affirming", tags=["saude_mental_adolescencia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_adole_gender_affirming","s":"ativo","d":"Gender Affirming","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_adole_gender_affirming"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
