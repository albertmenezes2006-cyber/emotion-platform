#!/usr/bin/env python3
"""Rich Club"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/rich_club", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_rich_club","s":"ativo","d":"Rich Club","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_rich_club"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
