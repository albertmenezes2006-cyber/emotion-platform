#!/usr/bin/env python3
"""Obstinacao Terapeutica em etica clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/etica_clinica/obstinacao_terapeutica", tags=["etica_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"etica_clinica_obstinacao_terapeutica","status":"ativo","desc":"Obstinacao Terapeutica em etica clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "etica_clinica_obstinacao_terapeutica"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
