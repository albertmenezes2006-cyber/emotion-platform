#!/usr/bin/env python3
"""Gerontopsicologia2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/gerontopsicologia2", tags=["saude_mental_idoso_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_idoso_gerontopsicologia2","s":"ativo","d":"Gerontopsicologia2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_idoso_gerontopsicologia2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
