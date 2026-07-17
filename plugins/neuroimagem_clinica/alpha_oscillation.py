#!/usr/bin/env python3
"""Alpha Oscillation"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/alpha_oscillation", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_alpha_oscillation","s":"ativo","d":"Alpha Oscillation","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_alpha_oscillation"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
