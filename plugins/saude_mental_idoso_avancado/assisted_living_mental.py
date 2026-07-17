#!/usr/bin/env python3
"""Assisted Living Mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/assisted_living_mental", tags=["saude_mental_idoso_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_idoso_assisted_living_mental","s":"ativo","d":"Assisted Living Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_idoso_assisted_living_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
