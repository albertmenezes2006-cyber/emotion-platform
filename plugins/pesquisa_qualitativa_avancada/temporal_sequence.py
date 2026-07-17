#!/usr/bin/env python3
"""Temporal Sequence"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/temporal_sequence", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_temporal_sequence","s":"ativo","d":"Temporal Sequence","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_temporal_sequence"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
