#!/usr/bin/env python3
"""Retrieval Cues"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/retrieval_cues", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_retrieval_cues","s":"ativo","d":"Retrieval Cues","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_retrieval_cues"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
