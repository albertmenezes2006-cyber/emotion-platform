#!/usr/bin/env python3
"""Parental Alienation Forensic"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/parental_alienation_forensic", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_parental_alienation_foren","s":"ativo","d":"Parental Alienation Forensic","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_parental_alienation_foren"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
