#!/usr/bin/env python3
"""Heidegger Analysis"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/heidegger_analysis", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_heidegger_analysis","s":"ativo","d":"Heidegger Analysis","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_heidegger_analysis"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
