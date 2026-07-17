#!/usr/bin/env python3
"""Efeitos psicológicos de medicamentos"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/med-efeitos", tags=["Populacoes"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "medicacao_efeitos", "status": "ativo",
                          "descricao": "Efeitos psicológicos de medicamentos",
                          "categoria": "populacoes",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "medicacao_efeitos",
                          "descricao": "Efeitos psicológicos de medicamentos",
                          "categoria": "populacoes",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "medicacao_efeitos"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
