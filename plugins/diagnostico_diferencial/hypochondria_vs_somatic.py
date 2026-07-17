#!/usr/bin/env python3
"""Hypochondria Vs Somatic"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/hypochondria_vs_somatic", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_hypochondria_vs_somatic","s":"ativo","d":"Hypochondria Vs Somatic","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_hypochondria_vs_somatic"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
