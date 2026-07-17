#!/usr/bin/env python3
"""Encoding Strategies"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/encoding_strategies", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_encoding_strategies","s":"ativo","d":"Encoding Strategies","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_encoding_strategies"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
