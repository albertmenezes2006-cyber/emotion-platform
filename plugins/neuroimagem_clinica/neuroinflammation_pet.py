#!/usr/bin/env python3
"""Neuroinflammation Pet"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/neuroinflammation_pet", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_neuroinflammation_pet","s":"ativo","d":"Neuroinflammation Pet","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_neuroinflammation_pet"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
