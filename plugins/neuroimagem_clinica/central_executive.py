#!/usr/bin/env python3
"""Central Executive"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/central_executive", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_central_executive","s":"ativo","d":"Central Executive","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_central_executive"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
