#!/usr/bin/env python3
"""Anxiety Vs Adhd"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/anxiety_vs_adhd", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_anxiety_vs_adhd","s":"ativo","d":"Anxiety Vs Adhd","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_anxiety_vs_adhd"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
