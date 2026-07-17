#!/usr/bin/env python3
"""DASS-21 Depressão Ansiedade Estresse"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/dass21", tags=["Avaliacao Avancada"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "dass21_triaxial", "status": "ativo",
                          "descricao": "DASS-21 Depressão Ansiedade Estresse",
                          "categoria": "avaliacao_avancada",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "dass21_triaxial",
                          "descricao": "DASS-21 Depressão Ansiedade Estresse",
                          "categoria": "avaliacao_avancada",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "dass21_triaxial"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
