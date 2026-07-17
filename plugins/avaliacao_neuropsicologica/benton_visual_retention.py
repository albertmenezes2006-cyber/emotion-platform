#!/usr/bin/env python3
"""Benton Visual Retention"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/benton_visual_retention", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_benton_visual_retention","s":"ativo","d":"Benton Visual Retention","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_benton_visual_retention"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
