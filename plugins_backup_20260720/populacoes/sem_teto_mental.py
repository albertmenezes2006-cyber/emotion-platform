#!/usr/bin/env python3
"""Saúde mental de pessoas em situação de rua"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/sem-teto", tags=["Populacoes"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "sem_teto_mental", "status": "ativo",
                          "descricao": "Saúde mental de pessoas em situação de rua",
                          "categoria": "populacoes",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "sem_teto_mental",
                          "descricao": "Saúde mental de pessoas em situação de rua",
                          "categoria": "populacoes",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "sem_teto_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
