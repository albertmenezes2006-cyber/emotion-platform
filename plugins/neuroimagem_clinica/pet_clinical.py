#!/usr/bin/env python3
"""Pet Clinical"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/pet_clinical", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_pet_clinical","s":"ativo","d":"Pet Clinical","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_pet_clinical"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
