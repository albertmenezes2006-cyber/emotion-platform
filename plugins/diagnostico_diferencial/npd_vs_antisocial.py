#!/usr/bin/env python3
"""Npd Vs Antisocial"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/npd_vs_antisocial", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_npd_vs_antisocial","s":"ativo","d":"Npd Vs Antisocial","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_npd_vs_antisocial"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
