#!/usr/bin/env python3
"""Perfectionism Self Compassion"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/mindfulness_/perfectionism_self_compassio", tags=["mindfulness_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"mindfulness_avanca_perfectionism_self_compas","s":"ativo","d":"Perfectionism Self Compassion","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "mindfulness_avanca_perfectionism_self_compas"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
