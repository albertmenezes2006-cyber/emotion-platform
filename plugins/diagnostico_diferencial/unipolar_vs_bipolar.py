#!/usr/bin/env python3
"""Unipolar Vs Bipolar"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/unipolar_vs_bipolar", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_unipolar_vs_bipolar","s":"ativo","d":"Unipolar Vs Bipolar","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_unipolar_vs_bipolar"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
