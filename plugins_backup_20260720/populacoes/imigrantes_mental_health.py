#!/usr/bin/env python3
"""Saúde mental de imigrantes"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/imigrantes-saude", tags=["Populacoes"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "imigrantes_mental_health", "status": "ativo",
                          "descricao": "Saúde mental de imigrantes",
                          "categoria": "populacoes",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "imigrantes_mental_health",
                          "descricao": "Saúde mental de imigrantes",
                          "categoria": "populacoes",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "imigrantes_mental_health"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
