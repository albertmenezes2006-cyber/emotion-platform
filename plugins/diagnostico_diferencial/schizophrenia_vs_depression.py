#!/usr/bin/env python3
"""Schizophrenia Vs Depression"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/schizophrenia_vs_depression", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_schizophrenia_vs_depressi","s":"ativo","d":"Schizophrenia Vs Depression","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_schizophrenia_vs_depressi"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
