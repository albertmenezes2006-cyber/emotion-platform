#!/usr/bin/env python3
"""Cortical Thickness Mri"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/cortical_thickness_mri", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_cortical_thickness_mri","s":"ativo","d":"Cortical Thickness Mri","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_cortical_thickness_mri"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
