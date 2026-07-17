#!/usr/bin/env python3
"""Symbol Search"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/symbol_search", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_symbol_search","s":"ativo","d":"Symbol Search","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_symbol_search"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
