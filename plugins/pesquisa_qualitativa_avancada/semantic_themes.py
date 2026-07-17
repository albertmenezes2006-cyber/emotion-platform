#!/usr/bin/env python3
"""Semantic Themes"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/semantic_themes", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_semantic_themes","s":"ativo","d":"Semantic Themes","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_semantic_themes"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
