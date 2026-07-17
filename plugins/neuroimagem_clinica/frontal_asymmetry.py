#!/usr/bin/env python3
"""Frontal Asymmetry"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/frontal_asymmetry", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_frontal_asymmetry","s":"ativo","d":"Frontal Asymmetry","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_frontal_asymmetry"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
