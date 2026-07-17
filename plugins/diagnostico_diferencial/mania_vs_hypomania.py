#!/usr/bin/env python3
"""Mania Vs Hypomania"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/mania_vs_hypomania", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_mania_vs_hypomania","s":"ativo","d":"Mania Vs Hypomania","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_mania_vs_hypomania"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
