#!/usr/bin/env python3
"""Formulation Feedback"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/formulation_feedback", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_formulation_feedback","s":"ativo","d":"Formulation Feedback","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_formulation_feedback"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
