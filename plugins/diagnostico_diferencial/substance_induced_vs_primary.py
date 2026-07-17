#!/usr/bin/env python3
"""Substance Induced Vs Primary"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/substance_induced_vs_primary", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_substance_induced_vs_prim","s":"ativo","d":"Substance Induced Vs Primary","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_substance_induced_vs_prim"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
