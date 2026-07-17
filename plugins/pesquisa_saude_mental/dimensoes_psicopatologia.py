#!/usr/bin/env python3
"""Dimensoes Psicopatologia em pesquisa saude mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_saude_/dimensoes_psicopatologia", tags=["pesquisa_saude_mental"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"pesquisa_saude_menta_dimensoes_psicopatologia","status":"ativo","desc":"Dimensoes Psicopatologia em pesquisa saude mental","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_saude_menta_dimensoes_psicopatologia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
