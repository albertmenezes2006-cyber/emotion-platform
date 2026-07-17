#!/usr/bin/env python3
"""Nao Maleficencia2 em etica clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/etica_clinica/nao_maleficencia2", tags=["etica_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"etica_clinica_nao_maleficencia2","status":"ativo","desc":"Nao Maleficencia2 em etica clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "etica_clinica_nao_maleficencia2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
