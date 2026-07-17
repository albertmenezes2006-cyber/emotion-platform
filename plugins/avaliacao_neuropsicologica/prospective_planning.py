#!/usr/bin/env python3
"""Prospective Planning"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/prospective_planning", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_prospective_planning","s":"ativo","d":"Prospective Planning","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_prospective_planning"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
