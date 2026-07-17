#!/usr/bin/env python3
"""Frontoparietal"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/frontoparietal", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_frontoparietal","s":"ativo","d":"Frontoparietal","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_frontoparietal"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
