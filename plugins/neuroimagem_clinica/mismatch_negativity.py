#!/usr/bin/env python3
"""Mismatch Negativity"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/mismatch_negativity", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_mismatch_negativity","s":"ativo","d":"Mismatch Negativity","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_mismatch_negativity"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
