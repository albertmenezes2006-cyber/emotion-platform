#!/usr/bin/env python3
"""Ventral Attention"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/ventral_attention", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_ventral_attention","s":"ativo","d":"Ventral Attention","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_ventral_attention"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
