#!/usr/bin/env python3
"""Information Subtest"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/information_subtest", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_information_subtest","s":"ativo","d":"Information Subtest","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_information_subtest"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
