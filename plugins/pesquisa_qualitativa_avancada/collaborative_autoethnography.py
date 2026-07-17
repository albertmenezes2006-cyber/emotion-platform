#!/usr/bin/env python3
"""Collaborative Autoethnography"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/collaborative_autoethnograph", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_collaborative_autoethnogr","s":"ativo","d":"Collaborative Autoethnography","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_collaborative_autoethnogr"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
