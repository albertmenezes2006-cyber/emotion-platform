#!/usr/bin/env python3
"""Performance Iq"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/performance_iq", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_performance_iq","s":"ativo","d":"Performance Iq","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_performance_iq"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
