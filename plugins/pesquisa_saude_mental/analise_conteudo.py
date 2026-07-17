#!/usr/bin/env python3
"""Analise Conteudo em pesquisa saude mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_saude_/analise_conteudo", tags=["pesquisa_saude_mental"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"pesquisa_saude_menta_analise_conteudo","status":"ativo","desc":"Analise Conteudo em pesquisa saude mental","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_saude_menta_analise_conteudo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
