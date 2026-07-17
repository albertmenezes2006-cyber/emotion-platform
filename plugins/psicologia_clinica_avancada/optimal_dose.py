#!/usr/bin/env python3
"""Optimal Dose"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/optimal_dose", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_optimal_dose","s":"ativo","d":"Optimal Dose","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_optimal_dose"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
