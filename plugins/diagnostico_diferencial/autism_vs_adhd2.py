#!/usr/bin/env python3
"""Autism Vs Adhd2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/autism_vs_adhd2", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_autism_vs_adhd2","s":"ativo","d":"Autism Vs Adhd2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_autism_vs_adhd2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
