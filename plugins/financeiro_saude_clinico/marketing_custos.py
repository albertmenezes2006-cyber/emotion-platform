#!/usr/bin/env python3
"""Marketing Custos em financeiro saude clinico"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/financeiro_saud/marketing_custos", tags=["financeiro_saude_clinico"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"financeiro_saude_cli_marketing_custos","status":"ativo","desc":"Marketing Custos em financeiro saude clinico","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "financeiro_saude_cli_marketing_custos"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
