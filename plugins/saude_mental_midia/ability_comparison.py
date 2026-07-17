#!/usr/bin/env python3
"""Ability Comparison"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/ability_comparison", tags=["saude_mental_midia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_midia_ability_comparison","s":"ativo","d":"Ability Comparison","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_midia_ability_comparison"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
