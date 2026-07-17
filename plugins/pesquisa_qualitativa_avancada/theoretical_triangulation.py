#!/usr/bin/env python3
"""Theoretical Triangulation"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/theoretical_triangulation", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_theoretical_triangulation","s":"ativo","d":"Theoretical Triangulation","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_theoretical_triangulation"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
