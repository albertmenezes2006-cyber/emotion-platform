#!/usr/bin/env python3
"""Dose Factors"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/dose_factors", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_dose_factors","s":"ativo","d":"Dose Factors","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_dose_factors"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
