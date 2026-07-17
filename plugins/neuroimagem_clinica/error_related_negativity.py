#!/usr/bin/env python3
"""Error Related Negativity"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/error_related_negativity", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_error_related_negativity","s":"ativo","d":"Error Related Negativity","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_error_related_negativity"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
