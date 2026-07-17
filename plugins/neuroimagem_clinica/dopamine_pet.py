#!/usr/bin/env python3
"""Dopamine Pet"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/dopamine_pet", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_dopamine_pet","s":"ativo","d":"Dopamine Pet","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_dopamine_pet"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
