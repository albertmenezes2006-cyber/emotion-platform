#!/usr/bin/env python3
"""Cognitive Flexibility Battery"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/cognitive_flexibility_batter", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_cognitive_flexibility_bat","s":"ativo","d":"Cognitive Flexibility Battery","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_cognitive_flexibility_bat"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
