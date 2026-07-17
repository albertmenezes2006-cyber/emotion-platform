#!/usr/bin/env python3
"""Temporal Order"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/temporal_order", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_temporal_order","s":"ativo","d":"Temporal Order","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_temporal_order"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
