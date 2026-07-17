#!/usr/bin/env python3
"""Casp Qualitative"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/casp_qualitative", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_casp_qualitative","s":"ativo","d":"Casp Qualitative","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_casp_qualitative"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
