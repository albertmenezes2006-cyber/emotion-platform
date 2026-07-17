#!/usr/bin/env python3
"""Anti Stigma Campaign"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/anti_stigma_campaign", tags=["saude_mental_midia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_midia_anti_stigma_campaign","s":"ativo","d":"Anti Stigma Campaign","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_midia_anti_stigma_campaign"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
