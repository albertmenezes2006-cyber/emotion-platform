#!/usr/bin/env python3
"""Dependent Vs Bpd"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/dependent_vs_bpd", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_dependent_vs_bpd","s":"ativo","d":"Dependent Vs Bpd","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_dependent_vs_bpd"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
