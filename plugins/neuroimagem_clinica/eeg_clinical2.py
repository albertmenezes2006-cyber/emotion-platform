#!/usr/bin/env python3
"""Eeg Clinical2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/eeg_clinical2", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_eeg_clinical2","s":"ativo","d":"Eeg Clinical2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_eeg_clinical2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
