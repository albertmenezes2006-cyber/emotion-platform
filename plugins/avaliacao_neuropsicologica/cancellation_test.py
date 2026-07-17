#!/usr/bin/env python3
"""Cancellation Test"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/cancellation_test", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_cancellation_test","s":"ativo","d":"Cancellation Test","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_cancellation_test"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
