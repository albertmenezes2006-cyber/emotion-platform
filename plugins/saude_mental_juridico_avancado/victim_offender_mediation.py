#!/usr/bin/env python3
"""Victim Offender Mediation"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/victim_offender_mediation", tags=["saude_mental_juridico_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_jurid_victim_offender_mediation","s":"ativo","d":"Victim Offender Mediation","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_jurid_victim_offender_mediation"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
