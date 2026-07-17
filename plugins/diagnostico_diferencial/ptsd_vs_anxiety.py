#!/usr/bin/env python3
"""Ptsd Vs Anxiety"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/ptsd_vs_anxiety", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_ptsd_vs_anxiety","s":"ativo","d":"Ptsd Vs Anxiety","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_ptsd_vs_anxiety"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
