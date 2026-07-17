#!/usr/bin/env python3
"""Deficiência intelectual e saúde"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/def-intelectual", tags=["Populacoes"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "deficiencia_intelectual", "status": "ativo",
                          "descricao": "Deficiência intelectual e saúde",
                          "categoria": "populacoes",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "deficiencia_intelectual",
                          "descricao": "Deficiência intelectual e saúde",
                          "categoria": "populacoes",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "deficiencia_intelectual"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
