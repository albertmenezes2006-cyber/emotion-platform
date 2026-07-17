#!/usr/bin/env python3
"""Boston Naming"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/boston_naming", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_boston_naming","s":"ativo","d":"Boston Naming","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_boston_naming"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
