#!/usr/bin/env python3
"""Processamento Texto Psi em pesquisa saude mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_saude_/processamento_texto_psi", tags=["pesquisa_saude_mental"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"pesquisa_saude_menta_processamento_texto_psi","status":"ativo","desc":"Processamento Texto Psi em pesquisa saude mental","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_saude_menta_processamento_texto_psi"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
