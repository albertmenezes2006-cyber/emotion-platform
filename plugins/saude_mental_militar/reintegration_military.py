#!/usr/bin/env python3
"""Reintegration Military"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/reintegration_military", tags=["saude_mental_militar"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_milit_reintegration_military","s":"ativo","d":"Reintegration Military","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_milit_reintegration_military"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
