#!/usr/bin/env python3
"""Refractory Cases"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/refractory_cases", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_refractory_cases","s":"ativo","d":"Refractory Cases","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_refractory_cases"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
