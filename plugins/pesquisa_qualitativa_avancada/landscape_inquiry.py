#!/usr/bin/env python3
"""Landscape Inquiry"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/landscape_inquiry", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_landscape_inquiry","s":"ativo","d":"Landscape Inquiry","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_landscape_inquiry"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
