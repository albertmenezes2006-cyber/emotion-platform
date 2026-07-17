#!/usr/bin/env python3
"""Doenca Infectocontagiosa em etica clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/etica_clinica/doenca_infectocontagiosa", tags=["etica_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"etica_clinica_doenca_infectocontagiosa","status":"ativo","desc":"Doenca Infectocontagiosa em etica clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "etica_clinica_doenca_infectocontagiosa"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
