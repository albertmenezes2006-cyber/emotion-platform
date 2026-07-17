#!/usr/bin/env python3
"""Autism Vs Social Anxiety"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/diagnostico_/autism_vs_social_anxiety", tags=["diagnostico_diferencial"])
@router.get("")
async def info():
    return JSONResponse({"p":"diagnostico_difere_autism_vs_social_anxiety","s":"ativo","d":"Autism Vs Social Anxiety","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "diagnostico_difere_autism_vs_social_anxiety"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
