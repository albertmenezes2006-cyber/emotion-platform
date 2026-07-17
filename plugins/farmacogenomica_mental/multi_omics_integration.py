#!/usr/bin/env python3
"""Multi Omics Integration"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/multi_omics_integration", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_multi_omics_integration","s":"ativo","d":"Multi Omics Integration","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_multi_omics_integration"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
