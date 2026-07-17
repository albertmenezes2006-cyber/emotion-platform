#!/usr/bin/env python3
"""Late Onset Depression"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/late_onset_depression", tags=["saude_mental_idoso_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_idoso_late_onset_depression","s":"ativo","d":"Late Onset Depression","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_idoso_late_onset_depression"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
