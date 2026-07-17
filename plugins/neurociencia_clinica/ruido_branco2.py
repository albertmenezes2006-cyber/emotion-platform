#!/usr/bin/env python3
"""Ruido Branco2 em neurociencia clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurociencia_cl/ruido_branco2", tags=["neurociencia_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"neurociencia_clinica_ruido_branco2","status":"ativo","desc":"Ruido Branco2 em neurociencia clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurociencia_clinica_ruido_branco2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
