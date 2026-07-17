#!/usr/bin/env python3
"""White Matter Mri"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/white_matter_mri", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_white_matter_mri","s":"ativo","d":"White Matter Mri","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_white_matter_mri"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
