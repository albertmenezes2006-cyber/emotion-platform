#!/usr/bin/env python3
"""Processing Speed Index"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/processing_speed_index", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_processing_speed_index","s":"ativo","d":"Processing Speed Index","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_processing_speed_index"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
