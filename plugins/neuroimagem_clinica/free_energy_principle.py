#!/usr/bin/env python3
"""Free Energy Principle"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/free_energy_principle", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_free_energy_principle","s":"ativo","d":"Free Energy Principle","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_free_energy_principle"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
