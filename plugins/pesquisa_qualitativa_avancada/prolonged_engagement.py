#!/usr/bin/env python3
"""Prolonged Engagement"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/prolonged_engagement", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_prolonged_engagement","s":"ativo","d":"Prolonged Engagement","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_prolonged_engagement"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
