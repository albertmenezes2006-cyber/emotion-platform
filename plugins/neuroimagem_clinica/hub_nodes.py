#!/usr/bin/env python3
"""Hub Nodes"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/hub_nodes", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_hub_nodes","s":"ativo","d":"Hub Nodes","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_hub_nodes"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
