#!/usr/bin/env python3
"""Adhd Vs Learning"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/adhd_vs_learning", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_adhd_vs_learning","s":"ativo","d":"Adhd Vs Learning","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_adhd_vs_learning"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
