#!/usr/bin/env python3
"""Downward Social Comparison"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/downward_social_comparison", tags=["saude_mental_midia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_midia_downward_social_compariso","s":"ativo","d":"Downward Social Comparison","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_midia_downward_social_compariso"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
