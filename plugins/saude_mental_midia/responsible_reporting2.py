#!/usr/bin/env python3
"""Responsible Reporting2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/responsible_reporting2", tags=["saude_mental_midia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_midia_responsible_reporting2","s":"ativo","d":"Responsible Reporting2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_midia_responsible_reporting2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
