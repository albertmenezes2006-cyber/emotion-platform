#!/usr/bin/env python3
"""Phq Ptsd Br em instrumentos avaliacao br"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/instrumentos_av/phq_ptsd_br", tags=["instrumentos_avaliacao_br"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"instrumentos_avaliac_phq_ptsd_br","status":"ativo","desc":"Phq Ptsd Br em instrumentos avaliacao br","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "instrumentos_avaliac_phq_ptsd_br"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
