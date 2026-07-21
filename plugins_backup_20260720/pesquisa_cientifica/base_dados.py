#!/usr/bin/env python3
"""Bases de dados científicos gratuitas"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/bases", tags=["Pesquisa Cientifica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "base_dados_psi", "status": "ativo",
                          "descricao": "Bases de dados científicos gratuitas",
                          "versao": "1.0.0",
                          "categoria": "pesquisa_cientifica",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "base_dados_psi"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
