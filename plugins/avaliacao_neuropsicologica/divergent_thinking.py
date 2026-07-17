#!/usr/bin/env python3
"""Divergent Thinking"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/divergent_thinking", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_divergent_thinking","s":"ativo","d":"Divergent Thinking","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_divergent_thinking"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
