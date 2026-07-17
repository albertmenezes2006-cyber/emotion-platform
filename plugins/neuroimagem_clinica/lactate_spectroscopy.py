#!/usr/bin/env python3
"""Lactate Spectroscopy"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/lactate_spectroscopy", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_lactate_spectroscopy","s":"ativo","d":"Lactate Spectroscopy","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_lactate_spectroscopy"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
