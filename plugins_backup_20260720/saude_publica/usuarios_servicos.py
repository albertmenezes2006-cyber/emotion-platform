#!/usr/bin/env python3
"""Usuários de serviços de saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/usuarios-sm", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "usuarios_servicos", "status": "ativo",
                          "descricao": "Usuários de serviços de saúde mental",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "usuarios_servicos",
                          "descricao": "Usuários de serviços de saúde mental",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "usuarios_servicos"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
