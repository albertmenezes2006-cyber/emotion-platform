#!/usr/bin/env python3
"""Hcr 20"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/hcr_20", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_hcr_20","s":"ativo","d":"Hcr 20","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_hcr_20"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
