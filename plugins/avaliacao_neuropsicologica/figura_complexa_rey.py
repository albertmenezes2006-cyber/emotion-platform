#!/usr/bin/env python3
"""Figura Complexa Rey"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/figura_complexa_rey", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_figura_complexa_rey","s":"ativo","d":"Figura Complexa Rey","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_figura_complexa_rey"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
