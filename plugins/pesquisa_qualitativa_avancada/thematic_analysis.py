#!/usr/bin/env python3
"""Thematic Analysis"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/thematic_analysis", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_thematic_analysis","s":"ativo","d":"Thematic Analysis","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_thematic_analysis"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
