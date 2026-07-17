#!/usr/bin/env python3
"""Lateralized Readiness"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/lateralized_readiness", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_lateralized_readiness","s":"ativo","d":"Lateralized Readiness","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_lateralized_readiness"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
