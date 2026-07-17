#!/usr/bin/env python3
"""Alzheimer Vs Dlb"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/alzheimer_vs_dlb", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_alzheimer_vs_dlb","s":"ativo","d":"Alzheimer Vs Dlb","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_alzheimer_vs_dlb"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
