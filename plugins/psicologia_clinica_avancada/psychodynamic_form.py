#!/usr/bin/env python3
"""Psychodynamic Form"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/psychodynamic_form", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_psychodynamic_form","s":"ativo","d":"Psychodynamic Form","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_psychodynamic_form"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
