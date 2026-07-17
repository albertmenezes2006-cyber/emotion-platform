#!/usr/bin/env python3
"""Verbal Iq"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/verbal_iq", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_verbal_iq","s":"ativo","d":"Verbal Iq","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_verbal_iq"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
