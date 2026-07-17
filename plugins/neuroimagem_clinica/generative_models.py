#!/usr/bin/env python3
"""Generative Models"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/generative_models", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_generative_models","s":"ativo","d":"Generative Models","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_generative_models"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
