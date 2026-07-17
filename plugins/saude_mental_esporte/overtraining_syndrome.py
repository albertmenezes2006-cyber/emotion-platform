#!/usr/bin/env python3
"""Overtraining Syndrome"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/overtraining_syndrome", tags=["saude_mental_esporte"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_espor_overtraining_syndrome","s":"ativo","d":"Overtraining Syndrome","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_espor_overtraining_syndrome"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
