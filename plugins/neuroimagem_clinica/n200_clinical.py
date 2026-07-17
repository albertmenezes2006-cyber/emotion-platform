#!/usr/bin/env python3
"""N200 Clinical"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/n200_clinical", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_n200_clinical","s":"ativo","d":"N200 Clinical","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_n200_clinical"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
