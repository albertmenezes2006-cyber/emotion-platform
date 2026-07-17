#!/usr/bin/env python3
"""Contingent Negative Variation"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/contingent_negative_variatio", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_contingent_negative_varia","s":"ativo","d":"Contingent Negative Variation","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_contingent_negative_varia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
