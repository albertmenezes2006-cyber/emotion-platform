#!/usr/bin/env python3
"""Ica Meg"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/ica_meg", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_ica_meg","s":"ativo","d":"Ica Meg","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_ica_meg"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
