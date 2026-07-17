#!/usr/bin/env python3
"""Sexual Behavior Dementia"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/sexual_behavior_dementia", tags=["saude_mental_idoso_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_idoso_sexual_behavior_dementia","s":"ativo","d":"Sexual Behavior Dementia","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_idoso_sexual_behavior_dementia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
