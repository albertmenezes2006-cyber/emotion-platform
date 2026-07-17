#!/usr/bin/env python3
"""Frontotemporal Battery"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/frontotemporal_battery", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_frontotemporal_battery","s":"ativo","d":"Frontotemporal Battery","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_frontotemporal_battery"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
