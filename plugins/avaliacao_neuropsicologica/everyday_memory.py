#!/usr/bin/env python3
"""Everyday Memory"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/everyday_memory", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_everyday_memory","s":"ativo","d":"Everyday Memory","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_everyday_memory"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
