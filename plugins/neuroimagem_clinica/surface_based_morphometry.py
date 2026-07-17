#!/usr/bin/env python3
"""Surface Based Morphometry"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/surface_based_morphometry", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_surface_based_morphometry","s":"ativo","d":"Surface Based Morphometry","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_surface_based_morphometry"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
