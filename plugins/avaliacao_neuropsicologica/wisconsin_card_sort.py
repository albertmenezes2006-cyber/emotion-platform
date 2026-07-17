#!/usr/bin/env python3
"""Wisconsin Card Sort"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/wisconsin_card_sort", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_wisconsin_card_sort","s":"ativo","d":"Wisconsin Card Sort","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_wisconsin_card_sort"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
