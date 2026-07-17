#!/usr/bin/env python3
"""Curso Online Receita em financeiro saude clinico"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/financeiro_saud/curso_online_receita", tags=["financeiro_saude_clinico"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"financeiro_saude_cli_curso_online_receita","status":"ativo","desc":"Curso Online Receita em financeiro saude clinico","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "financeiro_saude_cli_curso_online_receita"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
