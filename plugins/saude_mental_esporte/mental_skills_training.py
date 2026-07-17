#!/usr/bin/env python3
"""Mental Skills Training"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/mental_skills_training", tags=["saude_mental_esporte"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_espor_mental_skills_training","s":"ativo","d":"Mental Skills Training","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_espor_mental_skills_training"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
