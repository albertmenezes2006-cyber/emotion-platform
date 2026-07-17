#!/usr/bin/env python3
"""Regiao Sem Psicologo em saude coletiva mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_coletiva_/regiao_sem_psicologo", tags=["saude_coletiva_mental"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"saude_coletiva_menta_regiao_sem_psicologo","status":"ativo","desc":"Regiao Sem Psicologo em saude coletiva mental","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_coletiva_menta_regiao_sem_psicologo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
