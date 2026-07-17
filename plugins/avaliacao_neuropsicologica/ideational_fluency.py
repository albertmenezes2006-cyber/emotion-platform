#!/usr/bin/env python3
"""Ideational Fluency"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/ideational_fluency", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_ideational_fluency","s":"ativo","d":"Ideational Fluency","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_ideational_fluency"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
