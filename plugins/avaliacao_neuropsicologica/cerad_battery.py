#!/usr/bin/env python3
"""Cerad Battery"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/cerad_battery", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_cerad_battery","s":"ativo","d":"Cerad Battery","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_cerad_battery"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
