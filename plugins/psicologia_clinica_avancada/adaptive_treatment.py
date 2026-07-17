#!/usr/bin/env python3
"""Adaptive Treatment"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/adaptive_treatment", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_adaptive_treatment","s":"ativo","d":"Adaptive Treatment","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_adaptive_treatment"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
