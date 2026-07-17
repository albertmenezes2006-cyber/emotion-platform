#!/usr/bin/env python3
"""Aluguel Consultorio em financeiro saude clinico"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/financeiro_saud/aluguel_consultorio", tags=["financeiro_saude_clinico"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"financeiro_saude_cli_aluguel_consultorio","status":"ativo","desc":"Aluguel Consultorio em financeiro saude clinico","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "financeiro_saude_cli_aluguel_consultorio"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
