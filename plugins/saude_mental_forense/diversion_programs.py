#!/usr/bin/env python3
"""Diversion Programs"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/diversion_programs", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_diversion_programs","s":"ativo","d":"Diversion Programs","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_diversion_programs"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
