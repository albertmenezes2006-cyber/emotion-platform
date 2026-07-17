#!/usr/bin/env python3
"""Schizophrenia Vs Autism"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/schizophrenia_vs_autism", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_schizophrenia_vs_autism","s":"ativo","d":"Schizophrenia Vs Autism","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_schizophrenia_vs_autism"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
