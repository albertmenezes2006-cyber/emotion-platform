#!/usr/bin/env python3
"""Multiple Sclerosis Cog"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/multiple_sclerosis_cog", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_multiple_sclerosis_cog","s":"ativo","d":"Multiple Sclerosis Cog","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_multiple_sclerosis_cog"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
