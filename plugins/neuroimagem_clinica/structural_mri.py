#!/usr/bin/env python3
"""Structural Mri"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/structural_mri", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_structural_mri","s":"ativo","d":"Structural Mri","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_structural_mri"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
