#!/usr/bin/env python3
"""Structured Risk"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/structured_risk", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_structured_risk","s":"ativo","d":"Structured Risk","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_structured_risk"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
