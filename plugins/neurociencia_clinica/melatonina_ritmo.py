#!/usr/bin/env python3
"""Melatonina Ritmo em neurociencia clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurociencia_cl/melatonina_ritmo", tags=["neurociencia_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"neurociencia_clinica_melatonina_ritmo","status":"ativo","desc":"Melatonina Ritmo em neurociencia clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurociencia_clinica_melatonina_ritmo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
