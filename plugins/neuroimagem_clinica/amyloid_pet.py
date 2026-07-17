#!/usr/bin/env python3
"""Amyloid Pet"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/amyloid_pet", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_amyloid_pet","s":"ativo","d":"Amyloid Pet","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_amyloid_pet"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
