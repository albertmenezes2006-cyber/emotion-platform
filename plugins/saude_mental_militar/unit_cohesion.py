#!/usr/bin/env python3
"""Unit Cohesion"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/unit_cohesion", tags=["saude_mental_militar"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_milit_unit_cohesion","s":"ativo","d":"Unit Cohesion","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_milit_unit_cohesion"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
