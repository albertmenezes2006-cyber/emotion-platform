#!/usr/bin/env python3
"""Beta Oscillation2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/beta_oscillation2", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_beta_oscillation2","s":"ativo","d":"Beta Oscillation2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_beta_oscillation2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
