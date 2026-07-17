#!/usr/bin/env python3
"""Outcome Measures"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/outcome_measures", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_outcome_measures","s":"ativo","d":"Outcome Measures","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_outcome_measures"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
