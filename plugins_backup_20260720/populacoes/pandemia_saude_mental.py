#!/usr/bin/env python3
"""Saúde mental pós-pandemia"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/pandemia", tags=["Populacoes"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "pandemia_saude_mental", "status": "ativo",
                          "descricao": "Saúde mental pós-pandemia",
                          "categoria": "populacoes",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "pandemia_saude_mental",
                          "descricao": "Saúde mental pós-pandemia",
                          "categoria": "populacoes",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "pandemia_saude_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
