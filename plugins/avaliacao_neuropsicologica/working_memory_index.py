#!/usr/bin/env python3
"""Working Memory Index"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/working_memory_index", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_working_memory_index","s":"ativo","d":"Working Memory Index","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_working_memory_index"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
