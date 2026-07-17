#!/usr/bin/env python3
"""Adjacency Pairs"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/adjacency_pairs", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_adjacency_pairs","s":"ativo","d":"Adjacency Pairs","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_adjacency_pairs"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
