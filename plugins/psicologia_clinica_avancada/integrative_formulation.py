#!/usr/bin/env python3
"""Integrative Formulation"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/integrative_formulation", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_integrative_formulation","s":"ativo","d":"Integrative Formulation","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_integrative_formulation"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
