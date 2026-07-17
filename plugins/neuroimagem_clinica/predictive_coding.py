#!/usr/bin/env python3
"""Predictive Coding"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/predictive_coding", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_predictive_coding","s":"ativo","d":"Predictive Coding","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_predictive_coding"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
