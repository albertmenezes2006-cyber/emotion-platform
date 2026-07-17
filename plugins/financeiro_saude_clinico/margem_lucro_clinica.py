#!/usr/bin/env python3
"""Margem Lucro Clinica em financeiro saude clinico"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/financeiro_saud/margem_lucro_clinica", tags=["financeiro_saude_clinico"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"financeiro_saude_cli_margem_lucro_clinica","status":"ativo","desc":"Margem Lucro Clinica em financeiro saude clinico","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "financeiro_saude_cli_margem_lucro_clinica"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
