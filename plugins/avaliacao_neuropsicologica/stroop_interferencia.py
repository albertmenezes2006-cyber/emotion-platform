#!/usr/bin/env python3
"""Stroop Interferencia"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/stroop_interferencia", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_stroop_interferencia","s":"ativo","d":"Stroop Interferencia","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_stroop_interferencia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
