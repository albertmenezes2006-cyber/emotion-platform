#!/usr/bin/env python3
"""Therapist Effects"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/therapist_effects", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_therapist_effects","s":"ativo","d":"Therapist Effects","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_therapist_effects"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
