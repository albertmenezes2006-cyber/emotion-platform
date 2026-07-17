#!/usr/bin/env python3
"""Fmri Clinical"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/fmri_clinical", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_fmri_clinical","s":"ativo","d":"Fmri Clinical","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_fmri_clinical"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
