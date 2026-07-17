#!/usr/bin/env python3
"""Supervisao Obrigatoria em etica clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/etica_clinica/supervisao_obrigatoria", tags=["etica_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"etica_clinica_supervisao_obrigatoria","status":"ativo","desc":"Supervisao Obrigatoria em etica clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "etica_clinica_supervisao_obrigatoria"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
