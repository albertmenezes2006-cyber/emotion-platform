#!/usr/bin/env python3
"""Technique Factors"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/technique_factors", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_technique_factors","s":"ativo","d":"Technique Factors","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_technique_factors"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
