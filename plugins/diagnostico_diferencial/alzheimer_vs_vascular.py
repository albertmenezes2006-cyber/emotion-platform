#!/usr/bin/env python3
"""Alzheimer Vs Vascular"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/alzheimer_vs_vascular", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_alzheimer_vs_vascular","s":"ativo","d":"Alzheimer Vs Vascular","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_alzheimer_vs_vascular"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
