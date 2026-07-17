#!/usr/bin/env python3
"""Moca Blind"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/moca_blind", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_moca_blind","s":"ativo","d":"Moca Blind","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_moca_blind"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
