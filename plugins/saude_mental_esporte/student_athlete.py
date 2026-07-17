#!/usr/bin/env python3
"""Student Athlete"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/student_athlete", tags=["saude_mental_esporte"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_espor_student_athlete","s":"ativo","d":"Student Athlete","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_espor_student_athlete"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
