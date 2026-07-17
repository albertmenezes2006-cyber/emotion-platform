#!/usr/bin/env python3
"""Precision Weighting"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/precision_weighting", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_precision_weighting","s":"ativo","d":"Precision Weighting","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_precision_weighting"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
