#!/usr/bin/env python3
"""Tph1 Tph2 Serotonin"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/tph1_tph2_serotonin", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_tph1_tph2_serotonin","s":"ativo","d":"Tph1 Tph2 Serotonin","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_tph1_tph2_serotonin"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
