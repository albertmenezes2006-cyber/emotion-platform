#!/usr/bin/env python3
"""Oxitocina Confianca2 em neurociencia clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurociencia_cl/oxitocina_confianca2", tags=["neurociencia_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"neurociencia_clinica_oxitocina_confianca2","status":"ativo","desc":"Oxitocina Confianca2 em neurociencia clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurociencia_clinica_oxitocina_confianca2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
