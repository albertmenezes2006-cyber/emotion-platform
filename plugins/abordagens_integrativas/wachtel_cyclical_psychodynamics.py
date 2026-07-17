#!/usr/bin/env python3
"""Wachtel Cyclical Psychodynamics"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/wachtel_cyclical_psychodynam", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_wachtel_cyclical_psychody","s":"ativo","d":"Wachtel Cyclical Psychodynamics","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_wachtel_cyclical_psychody"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
