#!/usr/bin/env python3
"""Relatório para clínica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/relatorio-clinica", tags=["Relatorios Avancados"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "relatorio_clinica", "status": "ativo",
                          "descricao": "Relatório para clínica",
                          "versao": "1.0.0",
                          "categoria": "relatorios_avancados",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "relatorio_clinica"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
