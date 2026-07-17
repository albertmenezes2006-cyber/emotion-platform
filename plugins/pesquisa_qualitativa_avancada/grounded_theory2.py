#!/usr/bin/env python3
"""Grounded Theory2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/grounded_theory2", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_grounded_theory2","s":"ativo","d":"Grounded Theory2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_grounded_theory2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
