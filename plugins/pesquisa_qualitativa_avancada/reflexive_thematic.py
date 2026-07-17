#!/usr/bin/env python3
"""Reflexive Thematic"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/reflexive_thematic", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_reflexive_thematic","s":"ativo","d":"Reflexive Thematic","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_reflexive_thematic"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
