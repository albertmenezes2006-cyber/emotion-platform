#!/usr/bin/env python3
"""Ptsd Vs Dissociation"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/ptsd_vs_dissociation", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_ptsd_vs_dissociation","s":"ativo","d":"Ptsd Vs Dissociation","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_ptsd_vs_dissociation"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
