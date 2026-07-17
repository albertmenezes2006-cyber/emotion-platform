#!/usr/bin/env python3
"""Hierarchical Inference"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/hierarchical_inference", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_hierarchical_inference","s":"ativo","d":"Hierarchical Inference","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_hierarchical_inference"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
