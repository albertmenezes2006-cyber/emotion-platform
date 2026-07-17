#!/usr/bin/env python3
"""Wms Visual Reproduction"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/wms_visual_reproduction", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_wms_visual_reproduction","s":"ativo","d":"Wms Visual Reproduction","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_wms_visual_reproduction"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
