#!/usr/bin/env python3
"""Eixo Hpa em neurociencia clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurociencia_cl/eixo_hpa", tags=["neurociencia_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"neurociencia_clinica_eixo_hpa","status":"ativo","desc":"Eixo Hpa em neurociencia clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurociencia_clinica_eixo_hpa"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
