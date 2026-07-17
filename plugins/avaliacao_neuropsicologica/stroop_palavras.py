#!/usr/bin/env python3
"""Stroop Palavras"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/stroop_palavras", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_stroop_palavras","s":"ativo","d":"Stroop Palavras","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_stroop_palavras"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
