#!/usr/bin/env python3
"""Stai State em instrumentos avaliacao br"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/instrumentos_av/stai_state", tags=["instrumentos_avaliacao_br"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"instrumentos_avaliac_stai_state","status":"ativo","desc":"Stai State em instrumentos avaliacao br","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "instrumentos_avaliac_stai_state"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
