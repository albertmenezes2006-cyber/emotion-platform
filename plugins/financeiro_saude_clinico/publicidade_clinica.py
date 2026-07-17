#!/usr/bin/env python3
"""Publicidade Clinica em financeiro saude clinico"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/financeiro_saud/publicidade_clinica", tags=["financeiro_saude_clinico"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"financeiro_saude_cli_publicidade_clinica","status":"ativo","desc":"Publicidade Clinica em financeiro saude clinico","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "financeiro_saude_cli_publicidade_clinica"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
