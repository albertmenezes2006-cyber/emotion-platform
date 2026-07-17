#!/usr/bin/env python3
"""Professional Athlete Mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/professional_athlete_mental", tags=["saude_mental_esporte"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_espor_professional_athlete_ment","s":"ativo","d":"Professional Athlete Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_espor_professional_athlete_ment"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
