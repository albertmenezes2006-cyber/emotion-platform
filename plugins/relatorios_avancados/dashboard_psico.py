#!/usr/bin/env python3
"""Dashboard avançado do psicólogo"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/dashboard-psico", tags=["Relatorios Avancados"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "dashboard_psico_adv", "status": "ativo",
                          "descricao": "Dashboard avançado do psicólogo",
                          "versao": "1.0.0",
                          "categoria": "relatorios_avancados",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "dashboard_psico_adv"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
