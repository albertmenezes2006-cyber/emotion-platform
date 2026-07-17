#!/usr/bin/env python3
"""Ethnography2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/ethnography2", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_ethnography2","s":"ativo","d":"Ethnography2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_ethnography2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
