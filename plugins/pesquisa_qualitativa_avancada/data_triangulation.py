#!/usr/bin/env python3
"""Data Triangulation"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/data_triangulation", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_data_triangulation","s":"ativo","d":"Data Triangulation","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_data_triangulation"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
