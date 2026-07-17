#!/usr/bin/env python3
"""Analise Funcional Comportamento em tecnicas avaliacao"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/tecnicas_avalia/analise_funcional_comportament", tags=["tecnicas_avaliacao"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"tecnicas_avaliacao_analise_funcional_comport","status":"ativo","desc":"Analise Funcional Comportamento em tecnicas avaliacao","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "tecnicas_avaliacao_analise_funcional_comport"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
