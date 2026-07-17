#!/usr/bin/env python3
"""WHODAS 2.0 funcionalidade"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/whodas", tags=["Avaliacao Avancada"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "whodas_funcionalidade", "status": "ativo",
                          "descricao": "WHODAS 2.0 funcionalidade",
                          "categoria": "avaliacao_avancada",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "whodas_funcionalidade",
                          "descricao": "WHODAS 2.0 funcionalidade",
                          "categoria": "avaliacao_avancada",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "whodas_funcionalidade"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
