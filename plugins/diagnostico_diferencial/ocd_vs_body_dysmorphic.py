#!/usr/bin/env python3
"""Ocd Vs Body Dysmorphic"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/ocd_vs_body_dysmorphic", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_ocd_vs_body_dysmorphic","s":"ativo","d":"Ocd Vs Body Dysmorphic","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_ocd_vs_body_dysmorphic"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
