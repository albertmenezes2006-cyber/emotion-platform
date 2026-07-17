#!/usr/bin/env python3
"""Autism Spectrum"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/autism_spectrum", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_autism_spectrum","s":"ativo","d":"Autism Spectrum","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_autism_spectrum"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
