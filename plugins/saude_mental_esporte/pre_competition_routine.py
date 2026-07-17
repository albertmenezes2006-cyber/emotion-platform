#!/usr/bin/env python3
"""Pre Competition Routine"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/pre_competition_routine", tags=["saude_mental_esporte"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_espor_pre_competition_routine","s":"ativo","d":"Pre Competition Routine","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_espor_pre_competition_routine"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
