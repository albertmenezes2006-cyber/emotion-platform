#!/usr/bin/env python3
"""Dopamina Recompensa em neurociencia clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurociencia_cl/dopamina_recompensa", tags=["neurociencia_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"neurociencia_clinica_dopamina_recompensa","status":"ativo","desc":"Dopamina Recompensa em neurociencia clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurociencia_clinica_dopamina_recompensa"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
