#!/usr/bin/env python3
"""Duke Social Support em instrumentos avaliacao br"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/instrumentos_av/duke_social_support", tags=["instrumentos_avaliacao_br"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"instrumentos_avaliac_duke_social_support","status":"ativo","desc":"Duke Social Support em instrumentos avaliacao br","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "instrumentos_avaliac_duke_social_support"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
