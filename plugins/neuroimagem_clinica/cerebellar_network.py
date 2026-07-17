#!/usr/bin/env python3
"""Cerebellar Network"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/cerebellar_network", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_cerebellar_network","s":"ativo","d":"Cerebellar Network","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_cerebellar_network"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
