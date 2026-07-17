#!/usr/bin/env python3
"""Laissez Faire Leadership"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/laissez_faire_leadership", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_laissez_faire_leadership","s":"ativo","d":"Laissez Faire Leadership","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_laissez_faire_leadership"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
