#!/usr/bin/env python3
"""Reciprocal Translation"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/reciprocal_translation", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_reciprocal_translation","s":"ativo","d":"Reciprocal Translation","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_reciprocal_translation"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
