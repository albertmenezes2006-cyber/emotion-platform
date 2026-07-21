#!/usr/bin/env python3
"""Programa prevenção recaída"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/prev-recaida", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "programa_prevencao_recaida", "status": "ativo",
                          "descricao": "Programa prevenção recaída",
                          "categoria": "grupos",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "programa_prevencao_recaida",
                          "descricao": "Programa prevenção recaída",
                          "categoria": "grupos",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "programa_prevencao_recaida"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
