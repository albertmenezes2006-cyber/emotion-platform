#!/usr/bin/env python3
"""Remote Associates"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/remote_associates", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_remote_associates","s":"ativo","d":"Remote Associates","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_remote_associates"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
