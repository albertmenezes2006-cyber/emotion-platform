#!/usr/bin/env python3
"""Tcc Adicao Trabalho em intervencoes especificas"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/intervencoes_es/tcc_adicao_trabalho", tags=["intervencoes_especificas"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"intervencoes_especif_tcc_adicao_trabalho","status":"ativo","desc":"Tcc Adicao Trabalho em intervencoes especificas","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "intervencoes_especif_tcc_adicao_trabalho"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
