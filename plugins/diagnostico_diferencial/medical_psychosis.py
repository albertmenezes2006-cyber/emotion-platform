#!/usr/bin/env python3
"""Medical Psychosis"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/medical_psychosis", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_medical_psychosis","s":"ativo","d":"Medical Psychosis","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_medical_psychosis"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
