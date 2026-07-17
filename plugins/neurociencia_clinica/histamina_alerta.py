#!/usr/bin/env python3
"""Histamina Alerta em neurociencia clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurociencia_cl/histamina_alerta", tags=["neurociencia_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"neurociencia_clinica_histamina_alerta","status":"ativo","desc":"Histamina Alerta em neurociencia clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurociencia_clinica_histamina_alerta"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
