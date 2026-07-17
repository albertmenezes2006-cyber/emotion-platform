#!/usr/bin/env python3
"""Consolidation Assessment"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/consolidation_assessment", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_consolidation_assessment","s":"ativo","d":"Consolidation Assessment","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_consolidation_assessment"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
