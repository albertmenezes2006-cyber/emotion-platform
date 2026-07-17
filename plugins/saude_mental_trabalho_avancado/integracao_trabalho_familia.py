#!/usr/bin/env python3
"""Integracao Trabalho Familia em saude mental trabalho avancado"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental_tr/integracao_trabalho_familia", tags=["saude_mental_trabalho_avancado"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"saude_mental_trabalh_integracao_trabalho_famil","status":"ativo","desc":"Integracao Trabalho Familia em saude mental trabalho avancado","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_trabalh_integracao_trabalho_famil"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
