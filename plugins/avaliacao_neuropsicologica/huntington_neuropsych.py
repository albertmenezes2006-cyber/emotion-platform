#!/usr/bin/env python3
"""Huntington Neuropsych"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/huntington_neuropsych", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_huntington_neuropsych","s":"ativo","d":"Huntington Neuropsych","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_huntington_neuropsych"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
