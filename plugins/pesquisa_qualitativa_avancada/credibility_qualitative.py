#!/usr/bin/env python3
"""Credibility Qualitative"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/credibility_qualitative", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_credibility_qualitative","s":"ativo","d":"Credibility Qualitative","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_credibility_qualitative"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
