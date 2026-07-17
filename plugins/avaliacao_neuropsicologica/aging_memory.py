#!/usr/bin/env python3
"""Aging Memory"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/aging_memory", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_aging_memory","s":"ativo","d":"Aging Memory","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_aging_memory"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
