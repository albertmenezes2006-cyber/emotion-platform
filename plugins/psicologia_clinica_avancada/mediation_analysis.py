#!/usr/bin/env python3
"""Mediation Analysis"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/mediation_analysis", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_mediation_analysis","s":"ativo","d":"Mediation Analysis","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_mediation_analysis"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
