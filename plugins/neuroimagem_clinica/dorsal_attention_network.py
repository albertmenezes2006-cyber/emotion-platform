#!/usr/bin/env python3
"""Dorsal Attention Network"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/dorsal_attention_network", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_dorsal_attention_network","s":"ativo","d":"Dorsal Attention Network","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_dorsal_attention_network"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
