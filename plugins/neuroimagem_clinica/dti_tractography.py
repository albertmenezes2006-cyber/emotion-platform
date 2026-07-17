#!/usr/bin/env python3
"""Dti Tractography"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/dti_tractography", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_dti_tractography","s":"ativo","d":"Dti Tractography","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_dti_tractography"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
