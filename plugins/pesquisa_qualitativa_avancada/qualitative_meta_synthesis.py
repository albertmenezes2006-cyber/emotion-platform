#!/usr/bin/env python3
"""Qualitative Meta Synthesis"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/qualitative_meta_synthesis", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_qualitative_meta_synthesi","s":"ativo","d":"Qualitative Meta Synthesis","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_qualitative_meta_synthesi"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
