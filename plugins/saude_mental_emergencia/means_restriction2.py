#!/usr/bin/env python3
"""Means Restriction2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/means_restriction2", tags=["saude_mental_emergencia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_emerg_means_restriction2","s":"ativo","d":"Means Restriction2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_emerg_means_restriction2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
