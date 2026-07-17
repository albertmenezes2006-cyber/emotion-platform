#!/usr/bin/env python3
"""Psychosis Vs Mania"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/psychosis_vs_mania", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_psychosis_vs_mania","s":"ativo","d":"Psychosis Vs Mania","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_psychosis_vs_mania"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
