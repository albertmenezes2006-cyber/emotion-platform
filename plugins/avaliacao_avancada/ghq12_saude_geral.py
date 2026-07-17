#!/usr/bin/env python3
"""GHQ-12 saúde geral Goldberg"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/ghq12", tags=["Avaliacao Avancada"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "ghq12_saude_geral", "status": "ativo",
                          "descricao": "GHQ-12 saúde geral Goldberg",
                          "categoria": "avaliacao_avancada",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "ghq12_saude_geral",
                          "descricao": "GHQ-12 saúde geral Goldberg",
                          "categoria": "avaliacao_avancada",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "ghq12_saude_geral"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
