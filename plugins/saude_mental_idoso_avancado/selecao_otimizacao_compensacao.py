#!/usr/bin/env python3
"""Selecao Otimizacao Compensacao"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/selecao_otimizacao_compensac", tags=["saude_mental_idoso_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_idoso_selecao_otimizacao_compen","s":"ativo","d":"Selecao Otimizacao Compensacao","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_idoso_selecao_otimizacao_compen"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
