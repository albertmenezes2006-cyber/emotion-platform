#!/usr/bin/env python3
"""Dopamine Transporter"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/dopamine_transporter", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_dopamine_transporter","s":"ativo","d":"Dopamine Transporter","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_dopamine_transporter"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
