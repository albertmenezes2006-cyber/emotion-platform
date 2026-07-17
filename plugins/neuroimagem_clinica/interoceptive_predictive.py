#!/usr/bin/env python3
"""Interoceptive Predictive"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/interoceptive_predictive", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_interoceptive_predictive","s":"ativo","d":"Interoceptive Predictive","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_interoceptive_predictive"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
