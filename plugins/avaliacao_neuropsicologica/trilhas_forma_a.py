#!/usr/bin/env python3
"""Trilhas Forma A"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/trilhas_forma_a", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_trilhas_forma_a","s":"ativo","d":"Trilhas Forma A","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_trilhas_forma_a"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
