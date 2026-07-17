#!/usr/bin/env python3
"""Investigator Triangulation"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/investigator_triangulation", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_investigator_triangulatio","s":"ativo","d":"Investigator Triangulation","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_investigator_triangulatio"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
