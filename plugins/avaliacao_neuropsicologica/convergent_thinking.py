#!/usr/bin/env python3
"""Convergent Thinking"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/convergent_thinking", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_convergent_thinking","s":"ativo","d":"Convergent Thinking","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_convergent_thinking"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
