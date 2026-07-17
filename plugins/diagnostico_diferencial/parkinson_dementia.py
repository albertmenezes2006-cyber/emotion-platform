#!/usr/bin/env python3
"""Parkinson Dementia"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/parkinson_dementia", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_parkinson_dementia","s":"ativo","d":"Parkinson Dementia","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_parkinson_dementia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
