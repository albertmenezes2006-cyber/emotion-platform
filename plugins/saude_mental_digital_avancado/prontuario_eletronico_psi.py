#!/usr/bin/env python3
"""Prontuario Eletronico Psi em saude mental digital avancado"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental_di/prontuario_eletronico_psi", tags=["saude_mental_digital_avancado"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"saude_mental_digital_prontuario_eletronico_psi","status":"ativo","desc":"Prontuario Eletronico Psi em saude mental digital avancado","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_digital_prontuario_eletronico_psi"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
