#!/usr/bin/env python3
"""Capacidade Decisoria em etica clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/etica_clinica/capacidade_decisoria", tags=["etica_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"etica_clinica_capacidade_decisoria","status":"ativo","desc":"Capacidade Decisoria em etica clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "etica_clinica_capacidade_decisoria"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
