#!/usr/bin/env python3
"""Storied Lives"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/storied_lives", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_storied_lives","s":"ativo","d":"Storied Lives","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_storied_lives"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
