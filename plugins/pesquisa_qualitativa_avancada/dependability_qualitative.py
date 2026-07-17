#!/usr/bin/env python3
"""Dependability Qualitative"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/dependability_qualitative", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_dependability_qualitative","s":"ativo","d":"Dependability Qualitative","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_dependability_qualitative"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
