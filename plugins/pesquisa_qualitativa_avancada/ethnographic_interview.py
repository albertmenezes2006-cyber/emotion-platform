#!/usr/bin/env python3
"""Ethnographic Interview"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/ethnographic_interview", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_ethnographic_interview","s":"ativo","d":"Ethnographic Interview","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_ethnographic_interview"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
