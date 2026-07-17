#!/usr/bin/env python3
"""Stroop Cores"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/stroop_cores", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_stroop_cores","s":"ativo","d":"Stroop Cores","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_stroop_cores"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
