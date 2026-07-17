#!/usr/bin/env python3
"""Atenção e concentração avaliação"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/atencao-aval", tags=["Neuropsicologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "atencao_avaliacao", "status": "ativo",
                          "descricao": "Atenção e concentração avaliação",
                          "categoria": "neuropsicologia",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "atencao_avaliacao",
                          "descricao": "Atenção e concentração avaliação",
                          "categoria": "neuropsicologia",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "atencao_avaliacao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
