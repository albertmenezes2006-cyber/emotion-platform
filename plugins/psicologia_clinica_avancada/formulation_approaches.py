#!/usr/bin/env python3
"""Formulation Approaches"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/formulation_approaches", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_formulation_approaches","s":"ativo","d":"Formulation Approaches","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_formulation_approaches"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
