#!/usr/bin/env python3
"""Saúde mental em zonas de conflito"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/guerra", tags=["Populacoes"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "guerra_conflito_mental", "status": "ativo",
                          "descricao": "Saúde mental em zonas de conflito",
                          "categoria": "populacoes",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "guerra_conflito_mental",
                          "descricao": "Saúde mental em zonas de conflito",
                          "categoria": "populacoes",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "guerra_conflito_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
