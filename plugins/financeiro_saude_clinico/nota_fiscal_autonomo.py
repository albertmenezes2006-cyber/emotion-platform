#!/usr/bin/env python3
"""Nota Fiscal Autonomo em financeiro saude clinico"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/financeiro_saud/nota_fiscal_autonomo", tags=["financeiro_saude_clinico"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"financeiro_saude_cli_nota_fiscal_autonomo","status":"ativo","desc":"Nota Fiscal Autonomo em financeiro saude clinico","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "financeiro_saude_cli_nota_fiscal_autonomo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
