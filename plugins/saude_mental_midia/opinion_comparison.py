#!/usr/bin/env python3
"""Opinion Comparison"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/opinion_comparison", tags=["saude_mental_midia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_midia_opinion_comparison","s":"ativo","d":"Opinion Comparison","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_midia_opinion_comparison"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
