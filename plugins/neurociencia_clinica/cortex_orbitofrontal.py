#!/usr/bin/env python3
"""Cortex Orbitofrontal em neurociencia clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurociencia_cl/cortex_orbitofrontal", tags=["neurociencia_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"neurociencia_clinica_cortex_orbitofrontal","status":"ativo","desc":"Cortex Orbitofrontal em neurociencia clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurociencia_clinica_cortex_orbitofrontal"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
