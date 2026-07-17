#!/usr/bin/env python3
"""Discourse Analysis2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/discourse_analysis2", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_discourse_analysis2","s":"ativo","d":"Discourse Analysis2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_discourse_analysis2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
