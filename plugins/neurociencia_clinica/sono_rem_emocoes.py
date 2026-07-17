#!/usr/bin/env python3
"""Sono Rem Emocoes em neurociencia clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurociencia_cl/sono_rem_emocoes", tags=["neurociencia_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"neurociencia_clinica_sono_rem_emocoes","status":"ativo","desc":"Sono Rem Emocoes em neurociencia clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurociencia_clinica_sono_rem_emocoes"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
