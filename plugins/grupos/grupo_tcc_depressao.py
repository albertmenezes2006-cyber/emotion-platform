#!/usr/bin/env python3
"""Grupo TCC para depressão"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/grupo-tcc-dep", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "grupo_tcc_depressao", "status": "ativo",
                          "descricao": "Grupo TCC para depressão",
                          "categoria": "grupos",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "grupo_tcc_depressao",
                          "descricao": "Grupo TCC para depressão",
                          "categoria": "grupos",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "grupo_tcc_depressao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
