#!/usr/bin/env python3
"""Astrocitos Suporte em neurociencia clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurociencia_cl/astrocitos_suporte", tags=["neurociencia_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"neurociencia_clinica_astrocitos_suporte","status":"ativo","desc":"Astrocitos Suporte em neurociencia clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurociencia_clinica_astrocitos_suporte"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
