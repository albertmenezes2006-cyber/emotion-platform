#!/usr/bin/env python3
"""Luria Nebraska"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/luria_nebraska", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_luria_nebraska","s":"ativo","d":"Luria Nebraska","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_luria_nebraska"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
