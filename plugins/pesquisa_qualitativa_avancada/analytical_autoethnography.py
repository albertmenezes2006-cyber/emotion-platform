#!/usr/bin/env python3
"""Analytical Autoethnography"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/analytical_autoethnography", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_analytical_autoethnograph","s":"ativo","d":"Analytical Autoethnography","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_analytical_autoethnograph"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
