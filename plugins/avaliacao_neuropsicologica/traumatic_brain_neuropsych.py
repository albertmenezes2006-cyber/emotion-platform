#!/usr/bin/env python3
"""Traumatic Brain Neuropsych"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/traumatic_brain_neuropsych", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_traumatic_brain_neuropsyc","s":"ativo","d":"Traumatic Brain Neuropsych","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_traumatic_brain_neuropsyc"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
