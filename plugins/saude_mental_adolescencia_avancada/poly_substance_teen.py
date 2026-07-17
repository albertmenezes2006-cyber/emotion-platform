#!/usr/bin/env python3
"""Poly Substance Teen"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/poly_substance_teen", tags=["saude_mental_adolescencia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_adole_poly_substance_teen","s":"ativo","d":"Poly Substance Teen","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_adole_poly_substance_teen"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
