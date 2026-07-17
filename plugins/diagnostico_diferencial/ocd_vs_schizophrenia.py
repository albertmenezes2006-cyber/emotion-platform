#!/usr/bin/env python3
"""Ocd Vs Schizophrenia"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/ocd_vs_schizophrenia", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_ocd_vs_schizophrenia","s":"ativo","d":"Ocd Vs Schizophrenia","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_ocd_vs_schizophrenia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
