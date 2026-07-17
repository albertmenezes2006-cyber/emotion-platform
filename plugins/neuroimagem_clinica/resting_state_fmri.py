#!/usr/bin/env python3
"""Resting State Fmri"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/resting_state_fmri", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_resting_state_fmri","s":"ativo","d":"Resting State Fmri","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_resting_state_fmri"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
