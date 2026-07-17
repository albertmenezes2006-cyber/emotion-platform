#!/usr/bin/env python3
"""Nursing Home Mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/nursing_home_mental", tags=["saude_mental_idoso_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_idoso_nursing_home_mental","s":"ativo","d":"Nursing Home Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_idoso_nursing_home_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
