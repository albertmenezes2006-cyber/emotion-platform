#!/usr/bin/env python3
"""Comprehensive Soldier Fitness"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/comprehensive_soldier_fitnes", tags=["saude_mental_militar"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_milit_comprehensive_soldier_fit","s":"ativo","d":"Comprehensive Soldier Fitness","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_milit_comprehensive_soldier_fit"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
