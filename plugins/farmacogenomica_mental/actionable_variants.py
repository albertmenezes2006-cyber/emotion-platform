#!/usr/bin/env python3
"""Actionable Variants"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/actionable_variants", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_actionable_variants","s":"ativo","d":"Actionable Variants","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_actionable_variants"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
