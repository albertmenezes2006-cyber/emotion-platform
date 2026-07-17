#!/usr/bin/env python3
"""Epilepsy Neuropsych"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/epilepsy_neuropsych", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_epilepsy_neuropsych","s":"ativo","d":"Epilepsy Neuropsych","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_epilepsy_neuropsych"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
