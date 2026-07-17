#!/usr/bin/env python3
"""Active Inference"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/active_inference", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_active_inference","s":"ativo","d":"Active Inference","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_active_inference"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
