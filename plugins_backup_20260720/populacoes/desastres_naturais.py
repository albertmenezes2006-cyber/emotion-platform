#!/usr/bin/env python3
"""Saúde mental em desastres"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/desastres", tags=["Populacoes"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "desastres_naturais", "status": "ativo",
                          "descricao": "Saúde mental em desastres",
                          "categoria": "populacoes",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "desastres_naturais",
                          "descricao": "Saúde mental em desastres",
                          "categoria": "populacoes",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "desastres_naturais"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
