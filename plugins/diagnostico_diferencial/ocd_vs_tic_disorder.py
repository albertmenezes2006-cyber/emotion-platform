#!/usr/bin/env python3
"""Ocd Vs Tic Disorder"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/ocd_vs_tic_disorder", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_ocd_vs_tic_disorder","s":"ativo","d":"Ocd Vs Tic Disorder","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_ocd_vs_tic_disorder"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
