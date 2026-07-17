#!/usr/bin/env python3
"""Repair Sequences"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/repair_sequences", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_repair_sequences","s":"ativo","d":"Repair Sequences","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_repair_sequences"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
