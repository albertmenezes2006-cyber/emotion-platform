#!/usr/bin/env python3
"""Racismo estrutural e saúde"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/racismo-estrutural", tags=["Populacoes"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "racismo_estrutural_saude", "status": "ativo",
                          "descricao": "Racismo estrutural e saúde",
                          "categoria": "populacoes",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "racismo_estrutural_saude",
                          "descricao": "Racismo estrutural e saúde",
                          "categoria": "populacoes",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "racismo_estrutural_saude"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
