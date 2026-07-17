#!/usr/bin/env python3
"""Estabelecer limites saudáveis"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/limites", tags=["Relacionamentos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "limites_saudaveis", "status": "ativo",
                          "descricao": "Estabelecer limites saudáveis",
                          "versao": "1.0.0",
                          "categoria": "relacionamentos",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "limites_saudaveis"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
