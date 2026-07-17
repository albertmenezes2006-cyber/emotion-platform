#!/usr/bin/env python3
"""Recall Vs Recognition"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/recall_vs_recognition", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_recall_vs_recognition","s":"ativo","d":"Recall Vs Recognition","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_recall_vs_recognition"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
