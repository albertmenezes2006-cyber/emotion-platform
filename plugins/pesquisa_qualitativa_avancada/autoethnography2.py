#!/usr/bin/env python3
"""Autoethnography2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/autoethnography2", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_autoethnography2","s":"ativo","d":"Autoethnography2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_autoethnography2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
