#!/usr/bin/env python3
"""Perfusion Spect"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/perfusion_spect", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_perfusion_spect","s":"ativo","d":"Perfusion Spect","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_perfusion_spect"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
